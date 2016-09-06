var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
/**
 * Created by mrk2 on 04/09/2016.
 */
var Calculadora = (function () {
    function Calculadora() {
    }
    Calculadora.prototype.mostrarResultado = function (result) {
        console.log(result);
    };
    return Calculadora;
}());
var Operaciones = (function (_super) {
    __extends(Operaciones, _super);
    function Operaciones() {
        _super.apply(this, arguments);
    }
    Operaciones.metodoEstatico = function () {
        console.log('foo');
    };
    Operaciones.prototype.sum = function (a, b) {
        _super.prototype.mostrarResultado.call(this, a + b);
    };
    Operaciones.prototype.resta = function (a, b) {
        return a - b;
    };
    Operaciones.prototype.mult = function (a, b) {
        return a * b;
    };
    Operaciones.prototype.mostrarResultadoo = function (result) {
        console.log(result);
    };
    return Operaciones;
}(Calculadora));
var operacion = new Operaciones();
operacion.sum(2, 5);
var resultador = operacion.resta(4, 8);
var resultadom = operacion.mult(2, 5);
operacion.mostrarResultado(resultador);
operacion.mostrarResultadoo(resultadom);
Operaciones.metodoEstatico();
//# sourceMappingURL=hola.js.map