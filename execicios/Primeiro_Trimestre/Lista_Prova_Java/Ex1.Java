import java.util.Scanner;

public class Main {
    public static int soma(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um valor: ");
        int a = scanner.nextInt();

        System.out.print("Digite um segundo valor: ");
        int b = scanner.nextInt();

        System.out.println("Soma de " + a + " e " + b + " é " + soma(a, b));
    }
}

