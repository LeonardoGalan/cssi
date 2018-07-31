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


function Basic_Alarm(alarmMessage){
  return alarmMessage;
};
console.log(Basic_Alarm("My alarm!"));

function My_Alarm(wakeUp){
  return "Hey, Leo, wake up! It's " + wakeUp;

}
console.log(My_Alarm("9:00am"));

function Mom_Alarm(wakeMe){
  return "Hey, Mom, wake up! It's " + wakeMe;
}
console.log(Mom_Alarm("9:00am"));

function Family_Alarm(time,name){
  return "Hey, " + name+ ", wake up! It's " + time;

}
console.log(Family_Alarm("7:00am", "bro"));


function Important_Alarm(message){
  return message.toUpperCase();
}
console.log(Important_Alarm("wake up, wake up, wake up!!"))
