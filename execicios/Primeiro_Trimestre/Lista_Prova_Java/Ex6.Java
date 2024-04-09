import java.util.Scanner;

public class Main {
    public static int sum(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu primeiro número: ");
        int a = scanner.nextInt();

        System.out.print("Digite seu segundo número: ");
        int b = scanner.nextInt();

        System.out.print("Digite seu terceiro número: ");
        int c = scanner.nextInt();

        System.out.println("A soma dos números é: " + sum(a, b, c));
    }
}

