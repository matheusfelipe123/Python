import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a nota 1: ");
        int nota1 = scanner.nextInt();

        System.out.print("Digite a nota 2: ");
        int nota2 = scanner.nextInt();

        System.out.print("Digite a nota 3: ");
        int nota3 = scanner.nextInt();

        System.out.print("Digite a nota 4: ");
        int nota4 = scanner.nextInt();

        double media = (nota1 + nota2 + nota3 + nota4) / 4.0;

        System.out.println("Média: " + media);
    }
}

