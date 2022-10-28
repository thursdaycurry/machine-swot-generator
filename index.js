const strength = document.getElementById("strength");
const opportunity = document.getElementById("opportunity");
const weakness = document.getElementById("weakness");
const treat = document.getElementById("treat");

const so = document.getElementById("so");

window.addEventListener("keydown", function () {
  const sArr = strength.value.split("\n");
  const oArr = opportunity.value.split("\n");

  const result = [];

  console.log(sArr);
  console.log(oArr);

  for (let i = 0; i < sArr.length; i++) {
    for (let j = 0; j < oArr.length; j++) {
      result.push(`${sArr[i]} + ${oArr[j]}`);
    }
  }

  let analysis__text = "";
  result.forEach((el) => {
    analysis__text += `${el} \n`;
  });

  so.innerText = analysis__text;
});
