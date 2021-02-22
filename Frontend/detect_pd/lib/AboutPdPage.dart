import 'HelpNavBarTest.dart';
import 'SettingsNavBarTest.dart';
import 'package:flutter/material.dart';
import 'HomePage.dart';
import 'NavBar.dart';

void main() {
  runApp(MaterialApp(
      home: AboutPD(),
      theme: ThemeData(
        canvasColor: Color.fromRGBO(118, 176, 195, 100),
      )
  ));
}

class AboutPD extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: AboutPdForeground(
          expandedHeight: 153.0,
          appBarChild: Text('About PD'),
          appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
          fillChild: Text('drop-down, square buttons'),
          // fillColor:  Color.fromRGBO(240, 241, 226, 100),
          fillColor:  Color(0xff033e6b),
        ),
        bottomNavigationBar: NavBar(),
    );
  }
}

class AboutPdForeground extends StatelessWidget {
  final expandedHeight;
  final appBarChild;
  final appBarBackgroundColor;
  final fillChild;
  final fillColor;

  AboutPdForeground({this.expandedHeight, this.appBarBackgroundColor, this.appBarChild, this.fillChild, this.fillColor});

  @override
  Widget build(BuildContext context) {
    return CustomScrollView(
      slivers: <Widget>[
        SliverAppBar(
            backgroundColor:appBarBackgroundColor,
            expandedHeight: expandedHeight,
            floating: false,
            pinned: false,
            // title: appBarChild,
            flexibleSpace: FlexibleSpaceBar(
                background:HomeBackground(title: 'About PD' , height:130.0)
            )
        ),
        SliverFillRemaining(
          child: Container(
            width: MediaQuery.of(context).size.width,
            height: MediaQuery.of(context).size.height,
            color: appBarBackgroundColor,
            child: Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              decoration: BoxDecoration(
                color: fillColor,
                borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(40),
                    topRight: Radius.circular(40)
                ),
              ),
              // child: Center(
                child: Container(
                    child: Text("Parkinson's Disease \n\nLorem Ipsum is simply dummy "
                        "text of the printing and typesetting industry. Would you "
                        "like to take the guided test or continue? Lorem Ipsum is "
                        "simply dummy text of the printing and typesetting industry."
                        "Would you like to take the guided test or continue?",
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 20,
                    ),
                  ),
                  margin: EdgeInsets.all(30.0),
                  padding: EdgeInsets.all(10.0),
                  alignment: Alignment.topCenter,
                  width: 200,
                  height: 100,
              ),
            ),
          ),
        ),
      ],
    );
  }
}