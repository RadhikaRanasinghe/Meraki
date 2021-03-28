import 'package:detect_pd/services/api-firbase-storage.dart';
import 'package:ext_storage/ext_storage.dart';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:showcaseview/showcaseview.dart';
import 'package:detect_pd/widgets/showcaseview.dart';
import '../about-page.dart';
import '../camera-form-page.dart';
import '../faq-page.dart';
import '../gallery-form-page.dart';
import '../help-page.dart';
import 'package:detect_pd/globals.dart' as globals;
import 'package:detect_pd/services/api-firbase-storage.dart' as fire;

void main(){
  runApp(App());
}

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: ShowCaseWidget(builder: Builder(builder: (_) => NewSqaure())),
    );
  }
}

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
                  icon: Icons.upload_outlined),
            ),
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
                  icon: Icons.camera_alt_outlined),
            ),
            Flexible(
              child: SquareButtons(),
            ),
          ],
        ),
      ),
    );
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

class SquareButtons extends StatefulWidget {
  @override
  _SquareButtonsState createState() => _SquareButtonsState(
      EdgeInsets.all(50.0),
      EdgeInsets.all(0.0),
      EdgeInsets.all(8.0),
      60.0,
      14.0
  );
}

class _SquareButtonsState extends State<SquareButtons> {
  final padding;
  final bodyMargin;
  final buttonMargin;
  final iconSize;
  final fontSize;

  _SquareButtonsState(this.padding, this.bodyMargin, this.buttonMargin, this.iconSize, this.fontSize);

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
              onTap:(){
                Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => AboutPDPage()));
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
              side: BorderSide(color: Colors.grey, width: 1),
              borderRadius: BorderRadius.circular(20),
            ),
            color: Colors.grey,
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


