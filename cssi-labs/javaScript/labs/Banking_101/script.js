// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

function testMe(a){
  return a + 4;
};


let customer_name;
let balance;

function openAccount(name,startingBalance){
  balance = startingBalance;
  customer_name = name // Set the value for customer_name equal to name below

  let mystring = customer_name +" has opened a new account with a balance of $" + balance;
  return mystring; //write the statment you need to return here
}










function deposit(value = 100){
  // update the value of balance
    return customer_name +" has deposited " + value+". "+customer_name+"'s total balance is $"+ value;

  //return the correct statement
}

function withdraw(amount){
  //update the value of balance
    return name+"has withdrawn"+amount+"."+name+"has $" +balance+"remaining."//return the correct statement
}

// Write your script below
console.log("script is running...");


console.log(openAccount("Leo", 0));
console.log(deposit(100));
