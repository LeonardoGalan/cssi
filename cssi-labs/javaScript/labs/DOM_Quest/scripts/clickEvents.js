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


console.log("Running Click Events Script");
document.getElementById('box1').addEventListener('click',()=>{boxcolor(0);});
document.getElementById('box2').addEventListener('click',()=>{boxcolor(1);});
document.getElementById('box3').addEventListener('click',()=>{boxcolor(2);});
// document.getElementById('box4').addEventListener('click',()=>{ document.getElementById('box4').classList.toggle("active");});
document.getElementById('box5').addEventListener('click',()=>{boxcolor(4);});
//^ This is saying in the event of clicking box 1, box 2, 3,

let box4 = document.getElementById('box4');
box4.addEventListener('click',() => { box4.classList.toggle("active");});
let box5 = document.getElementById('box5');
box5.addEventListener('click',() => { box5.classList.toggle("active");});
//box5.addEventListener('click',() => {
  // box5.classList.toggle("active");
//   box4.classList.toggle("box");
//});


const colors = ['red','pink','orange'];

function boxcolor(value){ // the value specified in lines 17-20
  let newcolor = document.getElementsByClassName('box');
  newcolor[0].style.backgroundColor = colors[value];
  newcolor[1].style.backgroundColor = colors[value];
  newcolor[2].style.backgroundColor = colors[value];
}
// document.getElementById('box4').addEventListener('click',()=>boxcol('box4');});
// document.getElementById('box5').addEventListener('click',()=>boxcol('box4');});

function boxcol(value){
  let cg = document.getElementById(value).classList.toggle('active');


}
//
// {
//   box4.classList.toggle("active");
//   box5.classList.toggle("active");
//
//
// }
