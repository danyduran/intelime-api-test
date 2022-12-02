ALTER TABLE Restaurants ADD COLUMN geolocation geography(point);
UPDATE Restaurants SET geolocation=ST_MakePoint(lat, lng);


SELECT *
FROM restaurants
WHERE ST_DistanceSphere(ST_MakePoint(lng, lat), ST_MakePoint(-99.1270470974249, 19.4400570537131)) <= 150;

SELECT * FROM restaurants WHERE ST_DWithin(ST_SetSRID(ST_MakePoint(lng, lat),3785), ST_SetSRID(ST_MakePoint(-99.1270470974249, 19.4400570537131), 3785), 100);

SELECT * FROM restaurants 
  WHERE ST_DWithin(
    Geography(ST_MakePoint(lng, lat)),
    Geography(ST_MakePoint(-99.1270470974249, 19.4400570537131)),
    100
  );