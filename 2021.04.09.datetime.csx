using System.Threading;

// https://stackoverflow.com/questions/67027919/find-if-current-time-is-multiple-of-a-time-window-from-a-fixed-baseline
// TimeSpan start = new TimeSpan(9, 15, 0);
// Console.WriteLine(start);

DateTime start = DateTime.Now;
Console.WriteLine($"{start}: initializing start time");

int i = 0;
while(true){
    DateTime now = DateTime.Now;
    if (now.Second >= start.Second + 10){
        Console.WriteLine($"{now}: Enough time elapsed, resetting time");
        start = now;
    }
    else {
        Console.WriteLine($"{now}: Haven't reached the right time");
    }
    i+=1;
    Thread.Sleep(1000);
}