public class App {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        Circulo c1 = new Circulo(2, 1, 1, "rojo");
        Circulo c2 = new Circulo(4, 2, -2, "azul");

        System.out.println(c1);
        System.out.println(c2);
        System.out.println("Radio de c1: " + c1.getRadio());
        System.out.println("Diámetro de c1: " + c1.diametro());
        System.out.println("Perímetro de c2: " + c2.perimetro());
        System.out.println("Color de c1: " + c1.getColor());
        System.out.println("Área de c1: " + c1.area());
        System.out.println("Área de c2: " + c2.area());
    }
}

class Circulo {
    private double radio;
    private double xc;
    private double yc;
    private String color;

    public Circulo(double radio, double xc, double yc, String color) {
        this.radio = radio;
        this.xc = xc;
        this.yc = yc;
        this.color = color;
    }

    public double area() {
        return Math.PI * Math.pow(this.radio, 2);
    }

    public double perimetro() {
        return 2 * Math.PI * this.radio;
    }

    public double diametro() {
        return 2 * this.radio;
    }

    @Override
    public String toString() {
        return "Soy un círculo de radio " + this.radio + " y color " + this.color;
    }

    public double getRadio() {
        return radio;
    }

    public String getColor() {
        return color;
    }
}
