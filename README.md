> [!NOTE]
> Hello there! I decided to archive this repo unfinished. The large part of it because, **it doesn't work** + another software did backup better than mine.
> 
> My idea is to do entropy calculation before the compression process. In theory, this should allow for faster compression (for example, file with entropy of 8 is incompressible, so we can use something like `-mx=0`.) But in practice, entropy calculation cost CPU a lot. Which makes it 2x as slow as 7z at `-mx=9` compression settings.
> 
> Other than that, we already kinda solved Backup before. Software like [Borg](https://www.borgbackup.org/) did it.

# The UnCrap

An entropy-aware backup script backed with 7-Zip for compression and data encryption. Designed to be no-tools necessary for recovery (_other than 7-Zip that is_).

The name comes from Hellboy's quote, "Crap." Add **Un-** to it and you got me!

_Yes, I don't think I will change the name anytime soon._

> [!NOTE]
> This is still under construction, do not use. Plus, this tool is also designed for Linux only. But feel free to fork once its done.
