import 'package:flutter/material.dart';

void main(List<String> args) {
  runApp(new MaterialApp(
    home: MyApp(),
  ));
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SquareButtons(
        link1: null,
        link2: null,
        link3: null,
        link4: null,
        padding: EdgeInsets.all(30.0),
        bodyMargin: EdgeInsets.all(10.0),
        buttonMargin: EdgeInsets.all(8.0),
        iconSize: 70.0,
        fontSize: 14.0,
      ),
    );
  }
}

class SquareButtons extends StatelessWidget {
  final link1;
  final link2;
  final link3;
  final link4;
  final padding;
  final bodyMargin;
  final buttonMargin;
  final iconSize;
  final fontSize;

  SquareButtons({this.link1, this.link2, this.link3, this.link4, this.padding,
    this.bodyMargin, this.buttonMargin, this.iconSize, this.fontSize});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: padding,
        margin: bodyMargin,
        child: GridView.count(
          crossAxisCount: 2,
          children: <Widget>[
            Card(
              shape: RoundedRectangleBorder(
                side: BorderSide(color: Colors.white70, width: 1),
                borderRadius: BorderRadius.circular(20),
              ),
              color: Colors.black12,
              margin: buttonMargin,
              child: InkWell(
                onTap: (){
                  // ignore: unnecessary_statements
                  link1;
                },
                splashColor: Colors.green,
                child: Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: <Widget>[
                      Icon(Icons.file_download, size: iconSize,),
                      Text("Download Template", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                    ],
                  ),
                ),
              ),
            ),
            Card(
              shape: RoundedRectangleBorder(
                side: BorderSide(color: Colors.white70, width: 1),
                borderRadius: BorderRadius.circular(20),
              ),
              color: Colors.black12,
              margin: buttonMargin,
              child: InkWell(
                onTap: (){
                  // ignore: unnecessary_statements
                  link2;
                },
                splashColor: Colors.green,
                child: Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: <Widget>[
                      Icon(Icons.menu_book_sharp, size: iconSize,),
                      Text("About PD", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                    ],
                  ),
                ),
              ),
            ),
            Card(
              shape: RoundedRectangleBorder(
                side: BorderSide(color: Colors.white70, width: 1),
                borderRadius: BorderRadius.circular(20),
              ),
              color: Colors.black12,
              margin: buttonMargin,
              child: InkWell(
                onTap: (){
                  // ignore: unnecessary_statements
                  link3;
                },
                splashColor: Colors.green,
                child: Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: <Widget>[
                      Icon(Icons.find_in_page_rounded, size: iconSize,),
                      Text("User Guide", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                    ],
                  ),
                ),
              ),
            ),
            Card(
              shape: RoundedRectangleBorder(
                side: BorderSide(color: Colors.white70, width: 1),
                borderRadius: BorderRadius.circular(20),
              ),
              color: Colors.black12,
              margin: buttonMargin,
              child: InkWell(
                onTap: (){
                  // ignore: unnecessary_statements
                  link4;
                },
                splashColor: Colors.green,
                child: Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: <Widget>[
                      Icon(Icons.headset_mic_rounded, size: iconSize,),
                      Text("FAQ", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

