console.log('Welcome to Holberton School, what is your name?\n');
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
  process.stdin.end('This important software is now closing\n');
});
process.stdin.on('end', () => {

});
