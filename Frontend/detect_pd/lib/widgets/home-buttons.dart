import 'package:flutter/material.dart';

import '../about-page.dart';
import '../camera-form-page.dart';
import '../faq-page.dart';
import '../gallery-form-page.dart';
import '../help-page.dart';

void main(){
  runApp(App());
}

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: NewSquare(),
    );
  }
}

class NewSquare extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      // color: Colors.cyan,
      child: Center(
        child: Column(
          children: <Widget>[
            Container(
              width: 300.0,
              height: 70.0,
              margin: const EdgeInsets.only(left:30.0, top:30.0,right:30.0,bottom:5.0),
              child: RaisedButton.icon(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(100),
                    side: BorderSide(color: Colors.grey, width: 1)
                ),
                color: Colors.grey,
                icon: Icon(Icons.search_sharp, color: Colors.black),
                label: Text("START TEST",
                  style: TextStyle(
                      color: Colors.white70, fontSize: 25.0
                  ),
                ),
                padding: EdgeInsets.all(5.0),
                splashColor: null,
                elevation: 6.0,
                onPressed: null,
              ),
            ),
            Icon(Icons.arrow_drop_down, color: Colors.black, size: 30.0,),
            DropdownButton(buttonName:"Upload Photo", width: 260.0,
                height: 50.0,
                bodyMargin: const EdgeInsets.all(5.0),
                padding: EdgeInsets.all(5.0),
                elevation: 6.0,
                link: (){
                  Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => GalleryFormPage()));
                },
                icon: Icons.upload_outlined),
            DropdownButton(buttonName:"Take Photo", width: 260.0,
                height: 50.0,
                bodyMargin: const EdgeInsets.only(top: 5.0),
                padding: EdgeInsets.all(5.0),
                elevation: 6.0,
                link: (){
                  Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => CameraFormPage()));
                },
                icon: Icons.camera_alt_outlined),
            Flexible(
              child: SquareButtons(
                link1: null,
                link2: (){
                  Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => AboutPDPage()));
                },
                link3: (){
                  Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => HelpPage()));
                },
                link4: (){
                  Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => FaqPage()));
                },
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
    );
  }
}

class DropdownButton extends StatelessWidget{

  final String buttonName;
  final width;
  final height;
  final bodyMargin;
  final padding;
  final elevation;
  final link;
  final icon;
  final fontSize;

  DropdownButton({this.buttonName, this.width, this.height, this.bodyMargin, this.padding, this.elevation, this.link, this.icon, this.fontSize});

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
        icon: Icon(icon, color: Colors.black),
        label: Text(buttonName,
          style: TextStyle(
              color: Colors.white70, fontSize: fontSize
          ),
        ),
        padding: padding,
        splashColor: null,
        elevation: elevation,
        onPressed: link,
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
    return Container(
      height: 500.0,
      padding: padding,
      margin: bodyMargin,
      child: GridView.count(
        physics: NeverScrollableScrollPhysics(),
        crossAxisCount: 2,
        children: <Widget>[
          Card(
            shape: RoundedRectangleBorder(
              side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),
            color: Colors.grey,
            margin: buttonMargin,
            child: InkWell(
              onTap: link1,
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
              side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),
            color: Colors.grey,
            margin: buttonMargin,
            child: InkWell(
              onTap:link2,
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
              side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),
            color: Colors.grey,
            margin: buttonMargin,
            child: InkWell(
              onTap: link3,
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
              side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),
            color: Colors.grey,
            margin: buttonMargin,
            child: InkWell(
              onTap: link4,
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
    );
  }
}


