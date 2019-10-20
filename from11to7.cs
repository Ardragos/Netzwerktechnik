using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] y = new int[11];
            String x = Console.ReadLine();
            for(int i = 0; i<x.Length; i++)
            {
                y.SetValue(Int32.Parse(x.Substring(i, 1)), i);
            }
            Console.Write("Data is \"");
            for (int i = 0; i < y.Length; i++)
            {
                if (i == 3 || i == 7 || i > 8)
                {
                }
                else {
                    Console.Write(y[i]);
                }
            }
            Console.Write("\"");
        }
    }
}