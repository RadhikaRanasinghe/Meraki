import 'package:flutter/material.dart';

void main(){
  runApp(App());
}

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Buttons(),
    );
  }
}

class Buttons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        foregroundDecoration: BoxDecoration(borderRadius: BorderRadius.circular(20.0),
            border: Border.all(
            color: Colors.yellowAccent, width: 3.0
        )
        ),
        //height: 310.0,
        child: Center(
          child: Column(
            children: <Widget>[
              UploadPhoto(width: 250.0,
                  height: 50.12,
                  bodyMargin: const EdgeInsets.only(left:30.0, top:30.0,right:30.0,bottom:10.0),
                  padding: EdgeInsets.all(5.0),
                  elevation: 6.0,
                  link: null),
              TakePhoto(width: 250.0,
                  height: 50.12,
                  bodyMargin: const EdgeInsets.all(10.0),
                  padding: EdgeInsets.all(5.0),
                  elevation: 6.0,
                  link: null),
              Flexible(
                child: SquareButtons(
                  link1: null,
                  link2: null,
                  link3: null,
                  link4: null,
                  padding: EdgeInsets.all(50.0),
                  bodyMargin: EdgeInsets.all(0.0),
                  buttonMargin: EdgeInsets.all(8.0),
                  iconSize: 60.0,
                  fontSize: 14.0,
                ),
              ),
            ],
          ),
        ),
        decoration: BoxDecoration(
        borderRadius: BorderRadius.only(
        topLeft: Radius.circular(40),
        topRight: Radius.circular(40)
    ),
      ),
    ),
    );
  }
}

class TakePhoto extends StatelessWidget{

  final width;
  final height;
  final bodyMargin;
  final padding;
  final elevation;
  final link;

  TakePhoto({this.width, this.height, this.bodyMargin, this.padding, this.elevation, this.link});

  @override
  Widget build(BuildContext context) {

    return Container(
      width: width,
      height: height,
      margin: bodyMargin,
      child: RaisedButton.icon(
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(100),
            side: BorderSide(color: Colors.grey, width: 1)
        ),
        color: Colors.grey,
        icon: Icon(Icons.camera_alt_outlined),
        label: Text("Take Photo"),
        padding: padding,
        elevation: elevation,
        onPressed: (){
          // ignore: unnecessary_statements
          link;
        },
      ),
    );
  }

}
class UploadPhoto extends StatelessWidget{

  final width;
  final height;
  final bodyMargin;
  final padding;
  final elevation;
  final link;

  UploadPhoto({this.width, this.height, this.bodyMargin, this.padding, this.elevation, this.link});

  @override
  Widget build(BuildContext context) {

    return Container(
      width: width,
      height: height,
      margin: bodyMargin,
      child: RaisedButton.icon(
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(100),
            side: BorderSide(color: Colors.grey, width: 1)
        ),
        color: Colors.grey,
        icon: Icon(Icons.upload_outlined),
        label: Text("Upload Photo"),
        padding: padding,
        elevation: elevation,
        onPressed: (){
          // ignore: unnecessary_statements
          link;
        },
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
        height: 500.0,
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
                      Text("Download \nTemplate", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
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


