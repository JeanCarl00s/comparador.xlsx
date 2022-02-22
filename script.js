// Excel.run(function (context) {
//     var sheets = context.workbook.worksheets;
//     sheets.load("items/name");

//     return context.sync()
//         .then(function () {
//             if (sheets.items.length > 1) {
//                 console.log(`There are ${sheets.items.length} worksheets in the workbook:`);
//             } else {
//                 console.log(`There is one worksheet in the workbook:`);
//             }
//             sheets.items.forEach(function (sheet) {
//               console.log(sheet.name);
//             });
//         });
// }).catch(errorHandlerFunction);