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
        Console.WriteLine($"{i,3} {now}: Enough time elapsed, resetting time");
        start = now;
    }
    else {
        Console.WriteLine($"{i,3} {now}: Haven't reached the right time");
    }
    i+=1;
    Thread.Sleep(1000);
}

// would be nice to see a Timer implementation. Especially one that accounts for drift
// See https://stackoverflow.com/questions/1091710/c-sharp-timer-or-thread-sleep
// See https://docs.microsoft.com/en-us/dotnet/api/system.threading.timer