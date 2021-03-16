import 'package:flutter/material.dart';

// void main() => runApp(MaterialApp(
//   home: ResultBackgroundWidgetNeg(),
// ));
//
// class ResultBackgroundWidgetNeg extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: ResultBackground(
//         resultBackgroundHeight: 460.0,
//         resultBackgroundImage: 'assets/positiveBackground.png',
//       ),
//     );
//   }
// }

class ResultBackground extends StatelessWidget {
  final resultBackgroundHeight;
  final resultBackgroundImage;

  const ResultBackground({this.resultBackgroundHeight, this.resultBackgroundImage});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: resultBackgroundHeight,
      decoration: BoxDecoration(
          image: DecorationImage(
              image: AssetImage(resultBackgroundImage),
              fit: BoxFit.cover
          )
      ),
    );
  }
}