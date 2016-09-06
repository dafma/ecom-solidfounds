/**
 * Created by mrk2 on 04/09/2016.
 */
class Calculadora{
    public mostrarResultado(result: number){
        console.log(result);
    }
}

interface  Mate{
    uno: number;
    dos: number;
}


class Operaciones extends Calculadora implements Mate{
    uno: number;
    dos: number;
    static metodoEstatico(){
        console.log('foo');
    }

    public sum(a: number, b:number){
        super.mostrarResultado(a+b);
    }

    public resta(a: number, b:number){
        return a - b;
    }
    public mult(a: number, b:number){
        return a * b;
    }

    public mostrarResultadoo(result: number){
        console.log(result );
    }
}

let operacion = new Operaciones();
operacion.sum(2, 5);
let resultador = operacion.resta(4,8);
let resultadom = operacion.mult(2,5);
operacion.mostrarResultado( resultador);
operacion.mostrarResultadoo( resultadom);
Operaciones.metodoEstatico();