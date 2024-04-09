import java.util.Scanner;

public class Main {
    public static double area(int lado, int altura) {
        return (lado * altura) / 2.0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor do lado: ");
        int lado = scanner.nextInt();

        System.out.print("Digite o valor da altura: ");
        int altura = scanner.nextInt();

        System.out.println("Área do triângulo: " + area(lado, altura));
    }
}

