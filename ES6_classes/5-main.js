import Building from './5-building';

try {
  const b = new Building(100);
  console.log(b);
} catch (err) {
  console.log(err.message);
}

class TestBuilding extends Building {}

try {
  TestBuilding(200);
} catch (err) {
  console.log(err.message);
}
