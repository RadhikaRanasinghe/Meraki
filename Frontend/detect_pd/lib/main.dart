import 'package:flutter/material.dart';

void main() => runApp(PositiveBackground());

class PositiveBackground extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: Container(
        decoration: BoxDecoration(
            image: DecorationImage(
                image: AssetImage("lib/images/PositiveBackground2.png"),
                fit: BoxFit.cover)),
        child: Scaffold(
          backgroundColor: Colors.transparent,
          // appBar: AppBar(
          //   elevation: 0,
          //   backgroundColor: Colors.transparent,
          //   title: Text('My App'),
          //   centerTitle: true,
          //   leading: IconButton(
          //       icon: Icon(
          //         Icons.list,
          //         color: Colors.white,
          //       ),
          //       onPressed: () {}),
          // ),
        ),
      ),
    );
  }
}

// void main() => runApp(MaterialApp(
//   home: Text("Hey ninjas!"),
//
// ));

// void main() => runApp(BaseLayout());
//
// class BaseLayout extends StatelessWidget{
//   Widget build(BuildContext context) {
//     return MaterialApp(
//         home: Scaffold(
//             appBar: AppBar(
//                 title: Text('Set Full Screen Background Image')),
//             body: Center(
//
//             )
//         )
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//         home: Scaffold(
//             // appBar: AppBar(
//             //     title: Text('Set Full Screen Background Image')),
//             body: Center(
//
//                 child: Container(
//                     constraints: BoxConstraints.expand(),
//                     decoration: BoxDecoration(
//                         image: DecorationImage(
//                             image: AssetImage(""),
//                             fit: BoxFit.cover)
//                     ),
//                     child: Center(child: Text('Set Full Screen Background Image in Flutter',
//                       textAlign: TextAlign.center, style:
//                       TextStyle(color: Colors.brown, fontSize: 25, fontWeight: FontWeight.bold),),)
//                 )
//             )
//         )
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Container(
//         decoration: BoxDecoration(
//             image: DecorationImage(
//                 image: AssetImage("lib/images/confetti.png"),
//                 fit: BoxFit.cover
//           )
//         ),
//       ),
//     );
//   }
// }



