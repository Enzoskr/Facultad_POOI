package JavaProyects.Encapsulamiento;

public class Nota {
    private int valor;

    public Nota(int ValorInicial) {
        if(ValorInicial >= 0 && ValorInicial <= 10){
            this.valor = ValorInicial;
    }else {
        throw new IllegalArgumentException("El valor debe estar entre 0 y 10");
    }
}

    public int obtenervalor(){
        return valor;
    }
    public boolean aprobado(){
        return valor >= 4;
    }
    public boolean promocionado(){
        return valor >= 7;
    }

    public boolean desaprobado(){
        return !aprobado();
    }
   

    public static void main (String[] args) {
        Nota miNota = new Nota(8);
        System.out.println("Nota:" + miNota.obtenervalor());
        System.out.println("Aprobado:" + miNota.aprobado());
        System.out.println("Desaprobado:" + miNota.desaprobado());
        System.out.println("Promocionado:" + miNota.promocionado());
    }
}
