// Use "input()" to input a line from the user
// Use "input(str)" to print some text before requesting input
// You will need this in the following stages
const input = require('sync-input')

var coffeeMachine = {
  water: 400,
  milk: 540,
  beans: 120,
  cups: 9,
  money: 550
}

function remaining() {
  console.log(`The coffee machine has:
  ${coffeeMachine.water} ml of water
  ${coffeeMachine.milk} ml of milk
  ${coffeeMachine.beans} g of coffee beans
  ${coffeeMachine.cups} disposable cups
  $${coffeeMachine.money} of money\n`)
}

function makeCoffee(coffee) {
  for (let el in coffee) {
    if (coffeeMachine[el] < coffee[el]) {
      if (el !== 'money') {
        console.log(`Sorry, not enough ${el}!`)
        return;
      }
    }
  }
  console.log('I have enough resources, making you a coffee!\n')
  coffeeMachine.water -= coffee.water
  coffeeMachine.milk -= coffee.milk
  coffeeMachine.beans -= coffee.beans
  coffeeMachine.cups -= coffee.cups
  coffeeMachine.money += coffee.money
}

function buy() {
  let espresso = {water: 250, milk: 0, beans: 16, cups: 1, money: 4}
  let latte = {water: 350, milk: 75, beans: 20, cups: 1, money: 7}
  let cappuccino = {water: 200, milk: 100, beans: 12, cups: 1, money: 6}
  console.log('What do you want to buy? ' +
    '1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
  let coffeeType = Number(input())
  let coffee
  if (coffeeType === 1) {
    coffee = espresso
  } else if (coffeeType === 2) {
    coffee = latte
  } else if (coffeeType === 3) {
    coffee = cappuccino
  } else {
    return;
  }
  makeCoffee(coffee)
}

function fill() {
  let water = Number(input('Write how many ml of water you want to add:\n'))
  let milk = Number(input('Write how many ml of milk you want to add:\n'))
  let beans = Number(input('Write how many grams of coffee beans you want to add:\n'))
  let cups = Number(input('Write how many disposable coffee cups you want to add:\n'))
  coffeeMachine.water += water
  coffeeMachine.milk += milk
  coffeeMachine.beans += beans
  coffeeMachine.cups += cups
}

function take() {
  console.log(`I gave you ${coffeeMachine.money}\n`)
  coffeeMachine.money -= coffeeMachine.money
}

function main() {
  while (true) {
    console.log('Write action (buy, fill, take, remaining, exit):')
    let action = input()
    switch (action) {
      case 'buy':
        buy();
        break;
      case 'fill':
        fill();
        break;
      case 'take':
        take();
        break;
      case 'remaining':
        remaining();
        break;
      case 'exit':
        return;
    }
  }
}

main()