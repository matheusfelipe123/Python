import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu primeiro número: ");
        int numero1 = scanner.nextInt();

        System.out.print("Digite seu segundo número: ");
        int numero2 = scanner.nextInt();

        System.out.print("Digite seu terceiro número: ");
        int numero3 = scanner.nextInt();

        int maior;

        if (numero1 >= numero2 && numero1 >= numero3) {
            maior = numero1;
        } else if (numero2 >= numero1 && numero2 >= numero3) {
            maior = numero2;
        } else {
            maior = numero3;
        }

        System.out.println("O maior número é: " + maior);
    }
}

