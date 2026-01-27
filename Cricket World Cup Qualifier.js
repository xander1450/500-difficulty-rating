const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('', (input) => {
  const x = parseInt(input);
  if(x>=12){
      console.log("Yes");
  }else{
      console.log("No");
  }

  readline.close();
});