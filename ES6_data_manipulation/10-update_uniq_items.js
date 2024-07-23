function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('is not map');
  }

  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }

  return map;
}

module.exports = updateUniqueItems;
