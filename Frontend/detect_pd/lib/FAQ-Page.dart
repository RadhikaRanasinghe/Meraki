import 'package:detect_pd/HomeButtons.dart';
import 'package:detect_pd/settingsPage.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'home-Foreground.dart';
import 'home-background.dart';
import 'main.dart';
import 'navbar.dart';

// void main() => runApp(MaterialApp(
//   home: FaqPage(),
// ));

class FaqPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: HomeBackground(
          title: 'FAQ',
          logoPath: 'assets/pd_log_bg_small.png',
          height: 153.0,
          bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
          smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
          backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          titleColor: Colors.white,
        ),
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
        // fillChild: Buttons(),
        // fillChild: Settings(),
        fillChild: FaqForground(spacing:40.0),
        fillColor:  Color.fromRGBO(240, 241, 226, 100),
      ),
      bottomNavigationBar: NavBar(
        link1: null,
        link2: (){
          Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: (){
          Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SettingsPage()));
        },
        backgroundColor: Color.fromRGBO(240, 241, 226, 100) ,
      ),
    );
  }
}

class FaqForground extends StatelessWidget {

  final spacing;

  FaqForground({this.spacing});
  @override
  Widget build(BuildContext context) {
  return Container(

    child: new Center(

      child:Column(
          mainAxisAlignment: MainAxisAlignment.center,
        children:<Widget>[

          GreyButtons(buttonText:'Question 1'),
          SizedBox(height: spacing),
          GreyButtons(buttonText:'Question 2'),
          SizedBox(height: spacing),
          GreyButtons(buttonText:'Question 3'),
          SizedBox(height: spacing),
          GreyButtons(buttonText:'Question 4'),
          // GreyButtons()
        ]
      )
    )
  );


  }


}
class GreyButtons extends StatelessWidget {

  final buttonText;
  final function;

  GreyButtons({this.buttonText,this.function });


  @override
  Widget build(BuildContext context) {
    return Container(
      child: new Center(
        child: InkWell(
          onTap:(){
            // ignore: unnecessary_statements
            function;
          },
        child: Container(
       child: new Text(buttonText,
    style: TextStyle(
      color: Colors.white,
    )
       ),
                )
      ),
      ),
      width: 270.0,
      height: 46.0,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(33.0),
        color: const Color(0xff687b8d),
        boxShadow: [
          BoxShadow(
            color: const Color(0x29000000),
            offset: Offset(0, 3),
            blurRadius: 6,
          ),
        ],
      ),
    );

  }

  }
