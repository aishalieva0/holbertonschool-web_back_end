/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (const val of array) {
    array[idx] = appendString + val;
    idx++;
  }

  return array;
}
