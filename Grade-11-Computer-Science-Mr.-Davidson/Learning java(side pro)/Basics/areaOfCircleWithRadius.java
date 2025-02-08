package Basics;
import java.util.Scanner;

class areaOfCircleWithRadius {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int radius = scanner.nextInt();
        double area = (int) (Math.PI * Math.pow(radius, 2));
        System.out.println(area);
    }
}