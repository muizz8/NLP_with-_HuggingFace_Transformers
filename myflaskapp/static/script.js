function showInput(cardId) {
  var inputContainer = document.getElementById(cardId).getElementsByClassName('input-container')[0];
  var outputContainer = document.getElementById(cardId).getElementsByClassName('output-container')[0];
  inputContainer.style.display = 'flex';
  outputContainer.style.display = 'none';
  setTimeout(function() {
    // Do nothing, just wait
  }, 2000);
}

async function generateText(cardId) {
  var input = document.getElementById(cardId + 'Input').value;
  var response = await fetch('/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 'user_input': input }),
  });
  var data = await response.json();
  var output = data.result;
  document.getElementById(cardId + 'Output').value = output;
  document.getElementById(cardId).getElementsByClassName('output-container')[0].style.display = 'block';
  setTimeout(function() {
    // Do nothing, just wait
  }, 2000);
}

async function translateText(cardId) {
  var input = document.getElementById(cardId + 'Input').value;
  var language = document.getElementById('languages').value;
  
  // Map the select values to the expected values
  if (language === 'en-fr') {
    language = 'French';
  } else if (language === 'en-ur') {
    language = 'Urdu';
  }

  console.log(`Input: ${input}`);
  console.log(`Language: ${language}`);

  try {
    var response = await fetch('/translate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ 'user_input': input, 'target_language': language }),
    });

    console.log(`Response status: ${response.status}`);
    var data = await response.json();

    console.log(`Response data: ${JSON.stringify(data)}`);

    if (response.ok) {
      var output = data.result;
      document.getElementById(cardId + 'Output').value = output;
      document.getElementById(cardId).getElementsByClassName('output-container')[0].style.display = 'block';
    } else {
      document.getElementById(cardId + 'Output').value = `Error: ${data.error}`;
      console.error(`Translation error: ${data.error}`);
    }
  } catch (error) {
    console.error('Error during fetch:', error);
    document.getElementById(cardId + 'Output').value = `Error: ${error.message}`;
  }
}


async function summarizeText(cardId) {
  var input = document.getElementById(cardId + 'Input').value;
  var response = await fetch('/summarize', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 'user_input': input }),
  });
  var data = await response.json();
  var output = data.result;
  document.getElementById(cardId + 'Output').value = output;
  document.getElementById(cardId).getElementsByClassName('output-container')[0].style.display = 'block';
  setTimeout(function() {
    // Do nothing, just wait
  }, 2000);
}

async function analyzeSentiment(cardId) {
  var input = document.getElementById(cardId + 'Input').value;
  var response = await fetch('/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 'user_input': input }),
  });
  var data = await response.json();
  var output = data.result[0].label; // Adjusted to extract the sentiment label
  document.getElementById(cardId + 'Output').value = output;
  document.getElementById(cardId).getElementsByClassName('output-container')[0].style.display = 'block';
  setTimeout(function() {
    // Do nothing, just wait
  }, 2000);
}