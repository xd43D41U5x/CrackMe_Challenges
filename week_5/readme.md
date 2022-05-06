Ok, trying something different this week.  I first started looking at https://crackmes.one/crackme/612e85d833c5d41acedffa4f.  However, I found that it wasn't working the way it should based on the assembly review.  To add to that, it would act different depending on the Linux version (ELF file) you were using.  I think it has something to do with the way the compiler was trying to handle the float conversion in one portion, but am not sure.

Anyway, based on that, I decided to re-write it in C# and then test in C, both of which when compiled with Visual Studio rely on .NET, so it would be easy to see the src code with dnspy or dotpeek.  To avoid that and to mimic what actual attackers would do when they want a native exe (not written in .NET), I moved to C++.

Here I have ported the original and made a few improvements to correct some obvious issues in how it worked.  I also added one more fun/small twist since its easier to follow in assembly.

Here I have the exe you can reverse and also the c++ src code if you would like to compare that to the original.  I found that actually writing then reversing is helping with these a lot.  Writeup is included in this directory.
