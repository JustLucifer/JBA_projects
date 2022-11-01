function changeWord(toThisCase) {
  let currentText = document.getElementById('multitext');
  let listTokens = currentText.value.split(' ');

  let changedListTokens = [];
  listTokens.forEach(function(value){
    if (toThisCase === 'upper') {
      changedListTokens.push(value.toUpperCase());
    } else {
      changedListTokens.push(value.toLowerCase());
    }
  });

  currentText.value = changedListTokens.join(' ');
}

let toUpper = document.getElementById('upper-case');
toUpper.addEventListener('click', function() {
  changeWord('upper');
});

let toLower = document.getElementById('lower-case');
toLower.addEventListener('click', function() {
  changeWord('lower');
});

let toProper = document.getElementById('proper-case');
toProper.addEventListener('click', function() {
  let currentText = document.getElementById('multitext');
  let listTokens = currentText.value.split(' ');
  let changedListTokens = [];

  listTokens.forEach(function(value){
    let tmpValue = value.toLowerCase();
    let res = tmpValue.charAt(0).toUpperCase() + tmpValue.slice(1);
    changedListTokens.push(res);
  });

  currentText.value = changedListTokens.join(' ');
});

function findSentence(currentText) {
  let tmpListOfSentences = [];
  let splitStart = 0;

  for (let i = 0; i < currentText.value.length; i++) {
    let textValue = currentText.value;
    let char = textValue[i];

    if (char == '!' || char == '?' || char == '.') {
      let index = textValue.indexOf(char) + 1;
      tmpListOfSentences.push(textValue.slice(splitStart, index));
      splitStart = index;
    }
  }

  return tmpListOfSentences;
}

let toSentence = document.getElementById('sentence-case');
toSentence.addEventListener('click', function() {
  let currentText = document.getElementById('multitext');
  let listTokens = findSentence(currentText);
  
  let changedListTokens = [];

  listTokens.forEach(function(value){
    let tmpValue = value.toLowerCase();
    let firstChar = tmpValue.charAt(0);
    let res

    if (firstChar === ' ') {
      firstChar = tmpValue.charAt(1);
      res = firstChar.toUpperCase() + tmpValue.slice(2);
      changedListTokens.push(res);
    } else {
      res = tmpValue.charAt(0).toUpperCase() + tmpValue.slice(1);
      changedListTokens.push(res);
    }
  });

  currentText.value = changedListTokens.join(' ');
});

function download(filename, text) {
  let element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

let saveTextFile = document.getElementById('save-text-file');
saveTextFile.addEventListener('click', function() {
  let currentText = document.getElementById('multitext').value;
  download('text.txt', currentText);
});
  

