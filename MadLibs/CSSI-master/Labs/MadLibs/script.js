function init()
{
	document.getElementById("button1").addEventListener("click", generateMsg);/*Add Event Listener to button element that calls generateMsg() function*/
}


function generateMsg()
{
const idNames=["text1","text2","text3","text4","text5"];

let values = [];

for(let i = 0; i<idNames.length;i++)
{
	values[i] = document.getElementById(idNames[i]).value;


}//Create a constant array of the ids of the input textfields.*/


	/*Using a for loop, populate the values array with the values of the
	 textfields*/


	let msg = `If anybody is wondering, please know that I am <strong>${values[2]}</strong> at <strong>${values[4]}</strong> without you.
	You might want to consider <strong>${values[3]}</strong> <strong>${values[0]}</strong>... then again, you always preferred
	<strong>${values[1]}</strong>.`;

document.getElementById('msg').innerHTML=msg;	//Display the msg string in the paragraph element with id 'msg'
}
function generateMsg(document.body.style.backgroundColor = "red");
