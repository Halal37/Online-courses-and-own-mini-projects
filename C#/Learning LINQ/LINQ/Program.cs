using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Formats.Asn1;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using CsvHelper;
using CsvHelper.Configuration;

// ReSharper disable UseFormatSpecifierInInterpolation

namespace LINQ
{
    class Program
    {
        static void Main(string[] args)
        {
            string csvPath = @"D:\Dataset\googleplaystore1.csv";
            var googleApps = LoadGoogleAps(csvPath);

            // Display(googleApps);
            //GetData(googleApps);
            //ProjectData(googleApps);
            //   DivideData(googleApps);
            //     OrderData(googleApps);
            //    DataSetOperation(googleApps);
            //  DataVerification(googleApps);
            //GroupData(googleApps);
            GroupDataOperations(googleApps);

            var people = LoadPeople();
            var addresses = LoadAddresses();


            var joinedData = people.GroupJoin(addresses,
                p => p.Id,
                a => a.PersonId,
                (person, addresses) => new { person.Name, Addresses = addresses });

            foreach (var element in joinedData)
            {
                Console.WriteLine($"Name : {element.Name}");
                foreach (var address in element.Addresses)
                {
                    Console.WriteLine($"\t City: {address.City}, street: {address.Street}");
                }

            }

            Console.WriteLine();

        }

        private static List<Person> LoadPeople()
        {
            var currentDir = Directory.GetCurrentDirectory();
            var jsonFullPath = Path.GetRelativePath(currentDir, "Person/People.json");

            var json = File.ReadAllText(jsonFullPath);

            return JsonConvert.DeserializeObject<List<Person>>(json);
        }
        private static List<Address> LoadAddresses()
        {
            var currentDir = Directory.GetCurrentDirectory();
            var jsonFullPath = Path.GetRelativePath(currentDir, "Person/Addresses.json");

            var json = File.ReadAllText(jsonFullPath);

            return JsonConvert.DeserializeObject<List<Address>>(json);
        }

        static void GroupDataOperations(IEnumerable<GoogleApp> googleApps)
        {
            var categoryGroup = googleApps
                .GroupBy(e => e.Category);

            foreach (var group in categoryGroup)
            {
                var averageReviews = group.Average(g => g.Reviews);
                var minReviews = group.Min(g => g.Reviews);
                var maxReviews = group.Max(g => g.Reviews);

                var reviewsCount = group.Sum(g => g.Reviews);

                var allAppsFromGroupHaveRatingOfThree = group.All(a => a.Rating > 3.0);



                Console.WriteLine($"Category: {group.Key}");
                Console.WriteLine($"averageReviews: {averageReviews}");
                Console.WriteLine($"minReviews: {minReviews}");
                Console.WriteLine($"maxReviews: {maxReviews}");
                Console.WriteLine($"reviewsCount: {reviewsCount}");
                Console.WriteLine($"allAppsFromGroupHaveRatingOfThree: {allAppsFromGroupHaveRatingOfThree}");
                Console.WriteLine();

            }
        }
        static void GroupData(IEnumerable<GoogleApp> googleApps)
        {
            var categoryGroup = googleApps.GroupBy(e => new { e.Category, e.Type });

            foreach (var group in categoryGroup)
            {
                var key = group.Key;
                //var apps = artAndDesignGroup.Select(e => e);
                var apps = group.ToList();
                Console.WriteLine($"Displaing elements for group {group.Key.Category} , {group.Key.Type}");
                Display(apps);
            }
        }

        static void DataVerification(IEnumerable<GoogleApp> googleApps)
        {
            var allOperatorResult = googleApps.Where(a => a.Category == Category.WEATHER)
                .All(a => a.Reviews > 20);

            Console.WriteLine($"allOperatorResult {allOperatorResult}");


            var anyOperatorResult = googleApps.Where(a => a.Category == Category.WEATHER)
                .Any(a => a.Reviews > 3_000_000);

            Console.WriteLine($"anyOperatorResult {anyOperatorResult}");
        }


        static void DataSetOperation(IEnumerable<GoogleApp> googleApps)
        {
            var paidAppsCategories = googleApps.Where(a => a.Type == Type.Paid)
                .Select(a =>a.Category).Distinct();

            var setA = googleApps.Where(a => a.Rating > 4.7 && a.Type == Type.Paid && a.Reviews > 1000);
            var setB = googleApps.Where(a => a.Name.Contains("Pro") && a.Rating > 4.6 && a.Reviews > 10000);

           // Display(setA);
          //  Console.WriteLine("\n******");
          //  Display(setB);

            var appsUnion = setA.Union(setB);
            Display(appsUnion);

            var appsIntersect = setA.Intersect(setB);
            Display(appsIntersect);

            var appsExcept = setA.Except(setB);
            Display(appsExcept);

        }
        static void OrderData(IEnumerable<GoogleApp> googleApps)
        {
            var highRatedBeautyApps = googleApps.Where(app => app.Rating > 4.4 && app.Category == Category.BEAUTY);
            var sortedResults = highRatedBeautyApps.OrderByDescending(app => app.Rating)
                .ThenBy(app=> app.Name);
            Display(sortedResults);
        }
        static void DivideData(IEnumerable<GoogleApp> googleApps)
        {
            var highRatedBeautyApps = googleApps.Where(app => app.Rating > 4.6 && app.Category == Category.BEAUTY);

            var first5HighRatedBeautyApps = highRatedBeautyApps.Take(5);

            Display(first5HighRatedBeautyApps);
        }
        static void ProjectData(IEnumerable<GoogleApp> googleApps)
        {
            var highRatedApps = googleApps.Where(app => app.Rating > 4.6);
            var highRatedBeautyApps = highRatedApps.Where(highRatedApps => highRatedApps.Category == Category.BEAUTY);
            var highRatedBeautyAppsNames = highRatedBeautyApps.Select(highRatedBeautyApps => highRatedBeautyApps.Name);

            var dtos = highRatedBeautyApps.Select(app => new GoogleAppDto()
            {
                Reviews = app.Reviews,
                Name = app.Name

            });


            foreach (var dto in dtos)
            {
                Console.WriteLine($"{dto.Name}: {dto.Reviews}");
            }

            var anonymousdtos = highRatedBeautyApps.Select(app => new
            {
                Reviews = app.Reviews,
                Name = app.Name,
                Category = app.Category

            });

            foreach (var dto in anonymousdtos)
            {
                Console.WriteLine($"{dto.Name}: {dto.Reviews}: {dto.Category}");
            }

            var genres = highRatedBeautyApps.SelectMany(app => app.Genres);

            Console.WriteLine(string.Join(":", genres));

            Console.WriteLine(string.Join(", ", highRatedBeautyAppsNames));
        }
        static void GetData(IEnumerable<GoogleApp> googleApps)
        {
            var highRatedApps = googleApps.Where( app => app.Rating > 4.6);
            var highRatedBeautyApps = highRatedApps.Where(highRatedApps => highRatedApps.Category == Category.BEAUTY);
            Display(highRatedBeautyApps);

            var firstHighRatedBeautyApp = highRatedBeautyApps.FirstOrDefault(highRatedBeautyApps => highRatedBeautyApps.Reviews < 300);
            Console.WriteLine(firstHighRatedBeautyApp);
        }

        static void Display(IEnumerable<GoogleApp> googleApps)
        {
            foreach (var googleApp in googleApps)
            {
                Console.WriteLine(googleApp);
            }

        }
        static void Display(GoogleApp googleApp)
        {
            Console.WriteLine(googleApp);
        }

        static List<GoogleApp> LoadGoogleAps(string csvPath)
        {
            using (var reader = new StreamReader(csvPath))
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                csv.Context.RegisterClassMap<GoogleAppMap>();
                var records = csv.GetRecords<GoogleApp>().ToList();
                return records;
            }

        }

    }


}
