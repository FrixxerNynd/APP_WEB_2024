//Este es un comentario de una linea

/*Este es un comentario de
varias lineas */

//alerta
//alert("Soy una ventana de alerta")

//variables
var nombre="Fernando Jose Chavez Medina";
let nombre1="5 mas 5 patataaa";
let edad=20;
let logica=true;
let estatura=1.80;

//Mostrar en pantalla
let concatenacion= "La persona: "+nombre+", tiene la edad de: "+edad+" años.";

/*document.write(concatenacion+"<br>")
document.write("La persona: "+nombre+", tiene la edad de: "+edad+" años.");*/


//Mostrar en pantalla con document.getElemntbyID
let datos = document.getElementById("Informacion");
datos.innerHTML = `
<br>
<hr>
<h1> La persona: ${nombre}, tiene una edad de: ${edad} años</h1>
<hr>
<br>
`;

//let datos2 = document.getElementById("informacion2")
datos.innerHTML+= "<h2>La edad es: "+edad+"</h2>";

//Condicionales if
if(estatura >= 1.90)
{
    //document.write("Es una persona alta")
    datos.innerHTML+=` 
    <hr>
    <h3>Es una persona alta </h3>
    `;
}
else
    //document.write("Es una persona de estatura promedio")
    datos.innerHTML+=` 
        <hr>
        <h3>Es una persona de estatura promedio </h3>
        `;


//Ciclos

for(let i = 1;i <=5; i++)
{
    datos.innerHTML+=`<hr><h3>For: El numero es: ${i}</h3>`;
}

let i = 1
while(i<=5)
{
    datos.innerHTML+=`<hr><h3>While: El numero es: ${i}</h3>`;
    i++
}

i=1
do {
    datos.innerHTML+=`<hr><h3>DoWhile: El numero es: ${i}</h3>`;
    i++
} while (i<=5);

//Funciones:
//Funcion que no recibe parametros y no regresa valor
function suma(){
    let n1=2;
    let n2=4;
    suma = n1+n2;
    console.log("La suma es: "+suma);
    datos.innerHTML+= `<hr> <h3>La suma es ${suma}</h3>`;
}
suma();

//Funcione que no recibe parametros y regresa valor
function suma2(){
    let n1=2;
    let n2=4;
    suma = n1+n2;
    return suma
}
let sum= suma2();
datos.innerHTML+= `<hr> <h3>La suma 2 es ${sum}</h3>`;

//Funcion que recibe parametros y no regresa valor
function suma3(numero1, numero2){
    let n1=numero1;
    let n2=numero2;
    suma = n1+n2;
    datos.innerHTML+= `<hr> <h3>La suma 3 es ${suma}</h3>`;
}
suma3(3,4);

//Funcion que recibe parametros y regresa valor
function suma4(numero1, numero2){
    let n1=numero1;
    let n2=numero2;
    suma = n1+n2;
    return suma
}
sum= suma4(8,5);
datos.innerHTML+= `<hr> <h3>La suma 4 es ${sum}</h3>`;

//Arreglos
let animales = []
animales[0]= "Perico";
animales[1]= "Leon";
animales[2]= "Perro";
datos.innerHTML+=`
<hr> <h3>El rey de la selva es ${animales[1]}</h3>
`;


for(let i=0; i<animales.length; i++){
    datos.innerHTML+=`<hr> <h3>El rey de la selva es ${animales[i]}</h3>`;
}

animales.forEach(element => {
    datos.innerHTML+=`<hr> <h3>El rey de la selva es ${element}</h3>`;
});

//funcion de flecha
const sumaFlecha=(a,b)=>a+b;
datos.innerHTML+= `<hr> <h3>La suma 4 es ${sumaFlecha}</h3>`;
//funcion normal
function sumaR(a,b){
    return a+b
}
datos.innerHTML+= `<hr> <h3>La suma R es ${sumaR(3,6)}</h3>`;