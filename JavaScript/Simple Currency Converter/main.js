const input = require('sync-input');

function greeting() {
  console.log("Welcome to Currency Converter!\n" +
    "1 USD equals 1 USD\n" +
    "1 USD equals 113.5 JPY\n" +
    "1 USD equals 0.89 EUR\n" +
    "1 USD equals 74.36 RUB\n" +
    "1 USD equals 0.75 GBP");
}

function calcResult(amount, rate, fromCur=null) {
  if (fromCur) {
    amount = amount / fromCur * rate
    return amount.toFixed(4)
  }
}

function checkCurrencies(currs) {
  let from_ = input('From: ').toUpperCase();
  if (!Object.keys(currs).includes(from_)) {
    console.log('Unknown currency');
    return null
  }

  let to_ = input('To: ').toUpperCase();
  if (!Object.keys(currs).includes(to_)) {
    console.log('Unknown currency');
    return null
  }
  return {from: from_, to: to_}
}

function checkAmount() {
  let amount = Number(input('Amount: '))
  if (Number.isInteger(amount)) {
    if (amount >= 1) {
      return amount
    } else {
      console.log('The amount cannot be less than 1');
    }
  } else {
    console.log('The amount has to be a number');
  }
}

function convertCurrency() {
  let currencies = {
    USD: 1,
    JPY: 113.5,
    EUR: 0.89,
    RUB: 74.36,
    GBP: 0.75
  }
  while (true) {
    console.log('What do you want to convert?')
    let userCurrs = checkCurrencies(currencies)
    if (userCurrs != null) {
      let amount = checkAmount()
      if (amount) {
        let res = calcResult(amount,
          currencies[userCurrs.to],
          currencies[userCurrs.from]);
        console.log(`Result: ${amount} ${userCurrs.from} ` +
          `equals ${res} ${userCurrs.to}`)
        break
      }
    }
  }
}

function whatToDo() {
  while (true) {
    console.log('What do you want to do?\n' +
      '1-Convert currencies 2-Exit program')
    let toDo = input()
    if (toDo === '2') {
      console.log('Have a nice day!')
      break
    } else if (toDo === '1') {
      convertCurrency()
    } else {
      console.log('Unknown input')
    }
  }
}

greeting()
whatToDo()