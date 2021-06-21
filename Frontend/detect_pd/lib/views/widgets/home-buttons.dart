import 'package:detect_pd/services/api-firbase-storage.dart';
import 'package:ext_storage/ext_storage.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:showcaseview/showcaseview.dart';
import 'package:detect_pd/views/widgets/showcaseview.dart';
import 'package:detect_pd/views/ui/about-page.dart';
import 'package:detect_pd/views/ui/camera-form-page.dart';
import 'package:detect_pd/views/ui/faq-page.dart';
import 'package:detect_pd/views/ui/gallery-form-page.dart';
import 'package:detect_pd/views/ui/help-page.dart';
import 'package:detect_pd/utils/globals.dart' as globals;

class NewSqaure extends StatefulWidget {
  static const LAUNCH_STRING = "LAUNCH_STRING";

  @override
  _NewSqaureState createState() => _NewSqaureState();
}

class _NewSqaureState extends State<NewSqaure> {

  @override
  void initState(){
    super.initState();

    WidgetsBinding.instance.addPostFrameCallback(
            (_) => _isFirstLaunch().then((result){
          if(result){
            ShowCaseWidget.of(context).startShowCase([
              globals.keyThree,
              globals.keyOne,
              globals.keyTwo,
            ]);
          }
        }));
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Center(
        child: Column(
          children: <Widget>[
            Container(
                margin: EdgeInsets.only(top: 25.0),
                padding: EdgeInsets.all(25.0),
                // color: Colors.blueGrey,
                decoration: BoxDecoration(
                  color: Colors.blueGrey,
                  border: Border.all(
                    color: Colors.blueGrey,
                  ),
                  borderRadius: BorderRadius.circular(25.0),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.5),
                      spreadRadius: 3,
                      blurRadius: 4,
                      offset: Offset(0, 3), // changes position of shadow
                    ),
                  ],
              ),
              child: Column(
          children: <Widget>[
            Container(
              child: Padding(
                padding: const EdgeInsets.only(top: 0.0),
                child: Text("Start Test",
                  style: TextStyle(
                      color: Colors.white, fontSize: 25.0
                  ),
                ),
              ),
            ),
            Icon(Icons.arrow_drop_down, color: Colors.black, size: 30.0,),
            CustomShowcaseWidget(
              globalKey: globals.keyOne,
              description: 'Take test by uploading photo from Gallery',
              child: DropdownButton(buttonName:"Upload Photo", width: 260.0,
                  height: 50.0,
                  bodyMargin: const EdgeInsets.all(5.0),
                  padding: EdgeInsets.all(5.0),
                  elevation: 6.0,
                  link: (){
                    Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => GalleryFormPage()));
                  },
                  icon: Icons.upload_outlined), // DropdownButton
            ),  // CustomShowcaseWidget
            CustomShowcaseWidget(
              globalKey: globals.keyTwo,
              description: 'Take test by taking photo with Camera',
              child: DropdownButton(buttonName:"Take Photo", width: 260.0,
                  height: 50.0,
                  bodyMargin: const EdgeInsets.only(top: 5.0),
                  padding: EdgeInsets.all(5.0),
                  elevation: 6.0,
                  link: (){
                    Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => CameraFormPage()));
                  },
                  icon: Icons.camera_alt_outlined), // Dropdown
                  )
                ],
              ),
            ),
            Flexible(
              child: SquareButtons(),
            ),  // Flexible
          ],  // <Widget>[]
        ),  // Column
      ),  // Center
    );  // Container
  }

  Future<bool> _isFirstLaunch() async{
    final sharedPreferences = await SharedPreferences.getInstance();
    bool isFirstLaunch = sharedPreferences.getBool(NewSqaure.LAUNCH_STRING) ?? true;

    if(isFirstLaunch)
      sharedPreferences.setBool(NewSqaure.LAUNCH_STRING, false);

    return isFirstLaunch;
  }
}

class DropdownButton extends StatelessWidget{

  // creating the variables
  final String buttonName;
  final width;
  final height;
  final bodyMargin;
  final padding;
  final elevation;
  final link;
  final icon;
  final fontSize;

  // creating the constructor
  DropdownButton({this.buttonName, this.width, this.height, this.bodyMargin, this.padding, this.elevation, this.link, this.icon, this.fontSize});

  @override
  Widget build(BuildContext context) {

    return Container(
      width: width,
      height: height,
      margin: bodyMargin,
      // using the raised button widget with an icon
      child: RaisedButton.icon(
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(100),
            side: BorderSide(color: Colors.grey, width: 1)
        ),  // RoundedRectangleBorder
        color: Colors.grey,
        icon: Icon(icon, color: Colors.black),
        label: Text(buttonName,
          style: TextStyle(
              color: Colors.white70, fontSize: fontSize
          ),  // TextStyle
        ),  // Text
        padding: padding,
        splashColor: null,
        elevation: elevation,
        onPressed: link,
      ),  // RaisedButton.icon
    );  // Container
  }
}

class SquareButtons extends StatefulWidget {
  @override
  _SquareButtonsState createState() => _SquareButtonsState(
      EdgeInsets.only(right: 50.0, left: 50.0),
      EdgeInsets.all(0.0),
      EdgeInsets.all(8.0),
      60.0,
      14.0
  );  // _SquareButtonsState
}

class _SquareButtonsState extends State<SquareButtons> {

  // creating the variables
  final padding;
  final bodyMargin;
  final buttonMargin;
  final iconSize;
  final fontSize;

  // creating the constructor
  _SquareButtonsState(this.padding, this.bodyMargin, this.buttonMargin, this.iconSize, this.fontSize);

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 500.0,
      padding: padding,
      margin: bodyMargin,
      child: GridView.count(
        // disable the scrolling in grid view
        physics: NeverScrollableScrollPhysics(),
        crossAxisCount: 2,
        children: <Widget>[
          Card(
            shape: RoundedRectangleBorder(
              // side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),  // RoundedRectangleBorder
            color: Colors.blueGrey,
            margin: buttonMargin,
            child: InkWell(
              onTap: () async { // function to download meander template when button pressed
                getPermission(); // get permission to access device storage

                String path =
                await ExtStorage.getExternalStoragePublicDirectory(
                    ExtStorage.DIRECTORY_DOWNLOADS);
                String fullPath = "$path/MeanderTemplate.pdf";
                download2(dio, imgUrl, fullPath);

              },
              splashColor: Colors.green,
              child: Center(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: <Widget>[
                    CustomShowcaseWidget(description: 'Download Template before starting test',
                        globalKey: globals.keyThree,
                        child: Icon(Icons.file_download, size: iconSize,)),
                    Text("Download \nTemplate", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                  ],  // <Widget>[]
                ),  // Column
              ),  // Center
            ),  // Inkwell
          ),  // Card
          Card(
            shape: RoundedRectangleBorder(
              // side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),  // RoundedRectangleBorder
            color: Colors.blueGrey,
            margin: buttonMargin,
            child: InkWell(
              onTap:(){
                Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => AboutPDPage()));
              },
              splashColor: Colors.green,
              child: Center(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: <Widget>[
                    Icon(Icons.menu_book_sharp, size: iconSize,),
                    Text("About Us", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                  ],  // <Widget>[]
                ),  // Column
              ),  // Center
            ),  // Inkwell
          ),  // Card
          Card(
            shape: RoundedRectangleBorder(
              // side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),  // RoundedRectangleBorder
            color: Colors.blueGrey,
            margin: buttonMargin,
            child: InkWell(
              onTap: (){
                Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => HelpPage()));
              },
              splashColor: Colors.green,
              child: Center(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: <Widget>[
                    Icon(Icons.find_in_page_rounded, size: iconSize,),
                    Text("User Guide", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                  ],  // <Widget>[]
                ),  // Column
              ),  // Center
            ),  // Inkwell
          ),  // Card
          Card(
            shape: RoundedRectangleBorder(
              // side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),  // RoundedRectangleBorder
            color: Colors.blueGrey,
            margin: buttonMargin,
            child: InkWell(
              onTap: (){
                Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => FaqPage()));
              },
              splashColor: Colors.green,
              child: Center(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: <Widget>[
                    Icon(Icons.headset_mic_rounded, size: iconSize,),
                    Text("FAQ", style: new TextStyle(fontSize: fontSize, color: Colors.white),)
                  ],  // <Widget>[]
                ),  // Column
              ),  // Center
            ),  // InkWell
          ),  // Card
        ],  // <Widget>[]
      ),  // GridView.count
    );  // Container
  }
}


