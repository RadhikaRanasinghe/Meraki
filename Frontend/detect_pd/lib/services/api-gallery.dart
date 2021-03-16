import 'dart:convert';
import 'dart:io';
import 'package:detect_pd/loading-screen.dart';
import 'package:detect_pd/widgets/navbar.dart';
import 'package:dropdownfield/dropdownfield.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';
import 'package:detect_pd/widgets/home-foreground.dart';
import '../main.dart';
import '../neg-results-page.dart';
import '../pos-result-page.dart';
import '../settings-page.dart';


void main() {
  runApp(MaterialApp(
      home: GalleryFormPage(),
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        canvasColor: Color.fromRGBO(118, 176, 195, 100),
      )
  ));
}

// -------------------------------------------------------------------------- //
class GalleryFormPage extends StatefulWidget {
  @override
  _GalleryFormPageState createState() => _GalleryFormPageState();
}

class _GalleryFormPageState extends State<GalleryFormPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: null,
        appBarChild: Text('home Background'),
        appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
        fillChild: GalleryAccess(),
        // fillColor:  Color.fromRGBO(240, 241, 226, 100),
        fillColor:  Color(0xff82d5c1),
      ),
      bottomNavigationBar: NavBar(
        link1: null,
        link2: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => SettingsPage()));
        },
      ),
    );
  }
}


class GalleryAccess extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => GalleryAccessState();
}

class GalleryAccessState extends State<GalleryAccess> {
  File galleryFile;
  File image;
  final picker = ImagePicker();
  final TextEditingController ageController = TextEditingController();
  String gender;
  List genders = ["Male", "Female"];
  String handedness;
  List handednessList = ["Right-handed", "Left-handed"];

  Future<dynamic> pickImageFromGallery(ImageSource source) async {
    final image = await picker.getImage(source: source);

    setState(() {
      this.image = File(image.path);
    });
  }

  Future doUpload() async {
    // var request = http.MultipartRequest('POST', Uri.parse("http://detectpd.us-east-2.elasticbeanstalk.com/create_user"));
    var request = http.MultipartRequest('POST', Uri.parse("http://10.0.2.2:5000/create_user"));

    // creating request.fields
    request.fields['age'] = ageController.text;

    if (gender == "Male"){
      request.fields['gender'] = "1";
    } else {
      request.fields['gender'] = "2";
    }

    if (handedness == "Right-handed"){
      request.fields['handedness'] = "1";
    } else {
      request.fields['handedness'] = "2";
    }

    Map<String, String> headers = {"Content-type": "multipart/form-data", 'connection': 'keep-alive'};

    request.files.add(
      http.MultipartFile(
        'image',
        image.readAsBytes().asStream(),
        image.lengthSync(),
        filename: "filename",
        contentType: MediaType('image', 'jpg'),
      ),
    );

    request.headers.addAll(headers);
    print("request: " + request.toString());

    // send the POST request
    final resp = await request.send();
    print(resp.statusCode);
    String respStr = await resp.stream.bytesToString();
    print(respStr);

    // decode backend response from POST request
    final decodeRespStr = json.decode(respStr) as Map<String, dynamic>;
    int imageNo = decodeRespStr['image_no'];

    Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => (LoadingPage()))
    );

    //async function to perform http get
    // final response = await http.get('http://detectpd.us-east-2.elasticbeanstalk.com/retrieve_result?image_no=$imageNo'); //getting the response from our backend server script
    final response = await http.get('http://10.0.2.2:5000/retrieve_result?image_no=$imageNo'); //getting the response from our backend server script

    final decoded = json.decode(response.body) as Map<String, dynamic>; //converting it from json to key value pair

    if (decoded['result'] == false) {
      // display positive results page
      Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => PositiveResultsPage()));
    } else {
      // display negative results page
      Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => NegativeResultsPage()));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(32),
        child: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.only(
                  bottom: 35,
                ),
                child: Text(
                  "Enter the following",
                  style: TextStyle(
                    fontSize: 20,
                    color: const Color(0xFF033E6B),
                  ),
                ),
              ),
              Container(
                height: 70.0,
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                  color: Color.fromRGBO(118, 176, 195, 100),
                  borderRadius: BorderRadius.circular(10),
                  // border: Border.all(color: const Color(0xFF033E6B))
                ),
                child: TextField(
                  controller: ageController,
                  keyboardType: TextInputType.number,
                  decoration: new InputDecoration(
                    labelText: 'Age',
                    contentPadding: EdgeInsets.all(2.0),
                    focusedBorder: InputBorder.none,
                    enabledBorder: InputBorder.none,
                    // hintText: 'Age',
                    labelStyle: TextStyle(color: const Color(0xFF033E6B), fontSize: 18),
                    icon: Icon(Icons.add),
                  ),
                ),
              ),
              Container(
                // height: 70.0,
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                  color: Color.fromRGBO(118, 176, 195, 100),
                  borderRadius: BorderRadius.circular(10),
                  // border: Border.all(color: const Color(0xFF033E6B))
                ),
                child: Container(
                  width: 320.0,
                  height: 60.0,
                  padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                  margin: EdgeInsets.only(bottom: 5.0),
                  decoration: BoxDecoration(
                    color: Color.fromRGBO(118, 176, 195, 100),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: DropdownButton(
                    isExpanded: true,
                    hint: Text("Gender"),
                    dropdownColor: Colors.teal[200],
                    style: TextStyle(
                      color: const Color(0xFF033E6B),
                      fontSize: 18,
                    ),
                    value: gender,
                    onChanged: (newValue) {
                      setState(() {
                        gender = newValue;
                      });
                    },
                    items: genders.map((valueItem){
                      return DropdownMenuItem(
                        value: valueItem,
                        child: Text(valueItem),
                      );
                    }).toList(),
                    iconSize: 36,
                    underline: SizedBox(),
                    // icon: Icon(Icons.add)
                  ),
                ),
              ),
              Container(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                  color: Color.fromRGBO(118, 176, 195, 100),
                  borderRadius: BorderRadius.circular(10),
                  // border: Border.all(color: const Color(0xFF033E6B))
                ),
                child: Container(
                  width: 320.0,
                  height: 60.0,
                  padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                  margin: EdgeInsets.only(bottom: 5.0),
                  decoration: BoxDecoration(
                      color: Color.fromRGBO(118, 176, 195, 100),
                      borderRadius: BorderRadius.circular(10)),
                  child: DropdownButton(
                    isExpanded: true,
                    hint: Text("Handedness"),
                    dropdownColor: Colors.teal[200],
                    style: TextStyle(
                      color: const Color(0xFF033E6B),
                      fontSize: 18,
                    ),
                    value: handedness,
                    onChanged: (newValue) {
                      setState(() {
                        handedness = newValue;
                      });
                    },
                    items: handednessList.map((valueItem){
                      return DropdownMenuItem(
                        value: valueItem,
                        child: Text(valueItem),
                      );
                    }).toList(),
                    iconSize: 36,
                    underline: SizedBox(),
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsets.all(10.0),
                child: RaisedButton(
                  child: new Text('Select Image from Gallery'),
                  color: Colors.grey[400],
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(18.0),
                    // side: BorderSide(color: Colors.grey)
                  ),
                  onPressed: () => pickImageFromGallery(ImageSource.gallery),
                ),
              ),
              SizedBox(
                child: image == null
                    ? Center(child: new Text(''))
                    : Center(child: new Image.file(image)),
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: doUpload,
        child: Icon(Icons.add),
        backgroundColor: Colors.teal,
      ),
    );
  }
}
