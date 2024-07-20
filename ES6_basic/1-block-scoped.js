export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    console.log(`Task is: ${task}, Task2 is: ${task2}`);
  }

  return [task, task2];
}
