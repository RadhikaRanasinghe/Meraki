import 'dart:convert';
import 'dart:io';
import 'package:dropdownfield/dropdownfield.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';
import 'package:detect_pd/widgets/home-foreground.dart';
import '../neg-results-page.dart';
import '../pos-result-page.dart';

class GalleryAccess extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => GalleryAccessState();
}

class GalleryAccessState extends State<GalleryAccess> {
  File galleryFile;
  File image;
  final picker = ImagePicker();
  final TextEditingController ageController = TextEditingController();
  final TextEditingController genderController = TextEditingController();
  final TextEditingController handednessController = TextEditingController();
  String gender;
  List<String> genders = ["Male", "Female"];
  String handedness;
  List<String> handednessList = ["Right-handed", "Left-handed"];

  Future<dynamic> pickImageFromGallery(ImageSource source) async {
    final image = await picker.getImage(source: source);

    setState(() {
      this.image = File(image.path);
    });
  }

  doUpload() async {
    //TODO : Assign our API host address to this variable
    var request = http.MultipartRequest('POST', Uri.parse("http://10.0.2.2:5000/create_user"));

    request.fields['age'] = ageController.text;
    genderController.text = "Male" != null ? request.fields['gender'] = "1" : request.fields['gender'] = "2";
    handednessController.text = "Right-handed" != null ? request.fields['handedness'] = "1" : request.fields['handedness'] = "2";

    Map<String, String> headers = {"Content-type": "multipart/form-data", 'connection': 'keep-alive'};

    request.files.add(
      http.MultipartFile(
        'image',
        image.readAsBytes().asStream(),
        image.lengthSync(),
        filename: "filename",
        contentType: MediaType('image', 'jpeg'),
      ),
    );

    request.headers.addAll(headers);
    print("request: " + request.toString());

    // send the request
    request.send().then((value) => print(value.statusCode));

    // ------------------------------------------------------------------------- //
    // // TODO : Confirm if this is possible
    // //async function to perform http get
    // final response = await http.get('http://127.0.0.1:5000/retrieve_result'); //getting the response from our backend server script
    // final decoded = json.decode(response.body) as Map<String, dynamic>; //converting it from json to key value pair
    //
    // // Todo: complete method - if the result is positive display positive page, else display negative
    // if (decoded['Result'] == true) {
    //   // display positive results page
    //   Navigator.pushReplacement(
    //       context,
    //       MaterialPageRoute(builder: (context) => PositiveResultsPage()));
    // } else {
    //   // display negative results page
    //   Navigator.pushReplacement(
    //       context,
    //       MaterialPageRoute(builder: (context) => NegativeResultsPage()));
    // }
    // ------------------------------------------------------------------------- //

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
                    borderRadius: BorderRadius.circular(10)),
                child: TextField(
                  controller: ageController,
                  keyboardType: TextInputType.number,
                  decoration: new InputDecoration(
                    labelText: 'Age',
                    contentPadding: EdgeInsets.all(2.0),
                    focusedBorder: InputBorder.none,
                    enabledBorder: InputBorder.none,
                    // hintText: 'Age',
                    labelStyle: TextStyle(color: const Color(0xFF033E6B)),
                    icon: Icon(Icons.add),
                  ),
                ),
              ),
              Container(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                  color: Color.fromRGBO(118, 176, 195, 100),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: DropDownField(
                  controller: genderController,
                  onValueChanged: (dynamic value) {
                    gender = value;
                  },
                  value: gender,
                  required: true,
                  labelText: 'Gender',
                  labelStyle: TextStyle(color: const Color(0xFF033E6B)),
                  items: genders,
                  textStyle: TextStyle(color: Colors.black),
                  icon: Icon(Icons.add),
                ),
              ),
              Container(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                    color: Color.fromRGBO(118, 176, 195, 100),
                    borderRadius: BorderRadius.circular(10)),
                child: DropDownField(
                  controller: handednessController,
                  onValueChanged: (dynamic value) {
                    handedness = value;
                  },
                  value: handedness,
                  required: true,
                  labelText: 'Handedness',
                  labelStyle: TextStyle(color: const Color(0xFF033E6B)),
                  items: handednessList,
                  textStyle: TextStyle(color: Colors.black),
                  icon: Icon(Icons.add),
                ),
              ),
              Padding(
                padding: EdgeInsets.all(10.0),
                child: RaisedButton(
                  child: new Text('Select Image from Gallery'),
                  color: Colors.grey,
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
