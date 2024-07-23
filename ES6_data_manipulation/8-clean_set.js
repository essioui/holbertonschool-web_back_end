function cleanSet(set, startString) {

  if (typeof startString !== 'string') {
    return '';
  }

  return [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}

module.exports = cleanSet;
