using System;

namespace SimpleWebScrape
{
    class Program
    {
        static void Main(string[] args)
        {
            HtmlAgilityPack.HtmlWeb web = new HtmlAgilityPack.HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = web.Load("https://yts.mx");
            foreach(var i in doc.DocumentNode.SelectNodes("//a[@class='browse-movie-title']"))
            {
                Console.WriteLine(i.InnerText);
            }
        }
    }
}
