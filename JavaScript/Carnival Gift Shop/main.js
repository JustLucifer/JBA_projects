const input = require('sync-input');
let userTickets = 0;
let gifts = [
  { id: 1, name: "Teddy Bear", price: 10 },
  { id: 2, name: "Big Red Ball", price: 5 },
  { id: 3, name: "Huge Bear", price: 50 },
  { id: 4, name: "Candy", price: 8 },
  { id: 5, name: "Stuffed Tiger", price: 15 },
  { id: 6, name: "Stuffed Dragon", price: 30 },
  { id: 7, name: "Skateboard", price: 100 },
  { id: 8, name: "Toy Car", price: 25 },
  { id: 9, name: "Basketball", price: 20 },
  { id: 10, name: "Scary Mask", price: 75 }
];

function greetings() {
  console.log('WELCOME TO THE CARNIVAL GIFT SHOP!');
  console.log('Hello friend! Thank you for visiting the carnival!');
  showGifts();
}

function showGifts() {
  console.log("Here's the list of gifts:\n");

  if (checkGifts()) {
    return;
  }

  gifts.forEach(function(gift) {
    console.log(gift.id + "- " + gift.name + ", Cost: " + gift.price + " tickets");
  });
  console.log();
}

function checkGifts() {
  for (let i = 0; i <= gifts.length; i++) {
    if (gifts[i] !== undefined) {
      return false;
    }
  }
  console.log('Wow! There are no gifts to buy.\n');
  return true;
}

function buyGift() {
  if (checkGifts()) {
    return;
  }

  console.log('Enter the number of the gift you want to get: ');
  let numOfGift = +input() - 1;

  if (Number.isFinite(numOfGift)) {
    if (gifts[numOfGift] === undefined) {
      console.log('There is no gift with that number!\n');
    } else if (userTickets < gifts[numOfGift].price) {
      console.log("You don't have enough tickets to buy this gift.");
    } else {
      userTickets -= gifts[numOfGift].price;
      console.log(`Here you go, one ${gifts[numOfGift].name}!`);
      delete gifts[numOfGift];
      showTickets();
    }
  } else {
    console.log('Please enter a valid number!\n')
  }
}

function addTickets() {
  let amountTickets = +input('Enter the ticket amount: ');
  if (Number.isFinite(amountTickets) && 0 <= amountTickets && amountTickets <= 1000) {
    userTickets += amountTickets;
    showTickets();
  } else {
    console.log('Please enter a valid number between 0 and 1000.\n');
  }
}

function showTickets() {
  console.log(`Total tickets: ${userTickets}`);
}

function whatToDo() {
  while (true) {
    console.log('What do you want to do?');
    console.log('1-Buy a gift 2-Add tickets 3-Check tickets 4-Show gifts 5-Exit the shop');
    let answer = input();
    switch (answer) {
      case '1':
        buyGift();
        break;
      case '2':
        addTickets();
        break;
      case '3':
        showTickets();
        break;
      case '4':
        showGifts();
        break;
      case '5':
        return;
      default:
        console.log('Please enter a valid number!');
    }
  }
}

function bye() {
  console.log('Have a nice day!');
}

function main() {
  greetings();
  whatToDo();
  bye();
}

main();