% Code for trainig a model for the faces present in your data base and thus
% create a model from it which will be later used for prediction the code
% saves the model on the disk which can be later use for prediction of the
% test image fed to the system



global A;           % A matrix for storing the features of each face
global B;           % A matrix for storing label corresponding to the feature matrix A

A=[];               %empty initialization
B=[];               %empty initialization


%%%%%%%%%% Training %%%%%%%%%%


% Get a list of all files and folders in this folder.
files = dir('F:\r2015b\bin\AT&T');
% Get a logical vector that tells which is a directory.
dirFlags = [files.isdir];
% Extract only those that are directories.
subFolders = files(dirFlags);
% Print folder names to command window.


% loop for iterating the face database in order to perform training and get
% a model as a result
for k = 3 : length(subFolders)   % Outer loop iterate through Folders (face classes) 
    
    mydir=strcat('F:\r2015b\bin\AT&T\',subFolders(k).name); % this the directory containing the classes (folders) of each face
contents = dir(strcat(mydir,'\*.jpg'));         %Specify the extension of the images present in training database
X = java_array('java.lang.String', numel(contents));
for i = 1:numel(contents)          % Outer loop iterate through all the images in a single folder
  filename = contents(i).name;
  
  % Open the file specified in filename, do your processing...
  [path,name,ext] = fileparts(filename);
  DatabaseImage = imread(strcat(strcat(mydir,'\'),strcat(name,ext)));
lbptest = preprocessing(DatabaseImage);             % get a feature vector (HOG features)

if i==1
    
  

  l= vec2mat(lbptest,length(lbptest));   % Convert feature vector into matrix to make input competible for training funcrion
    
     m= subFolders(k).name;   
     
     A=[A;l];                             %Add feature row into matrix
     B=[B;m];                             % Add label row into matrix
     
else 
    l= vec2mat(lbptest,length(lbptest));        
      m = subFolders(k).name;
A=[A;l];
B=[B;m];
end
end
fprintf('Sub folder #%d = %s\n', k, subFolders(k).name);
end





SVMModel = fitcecoc(A,B);       % create SVM model
svmstruct=SVMModel;             % create object of SVM model for saving it on the disk
save('latestmodel.mat','svmstruct');    % saving SVM model on the disk



%%%%%%%%%% Testing %%%%%%%%%%

    mydir='F:\r2015b\bin\communication';      % Directory containing test image  
contents = dir(strcat(mydir,'\*.jpg'));       % extension of the test images in the directory
X = java_array('java.lang.String', numel(contents));
for i = 1:numel(contents)
  filename = contents(i).name;
  % Open the file specified in filename, do your processing...
  [path,name,ext] = fileparts(filename);
  DatabaseImage = imread(strcat(strcat(mydir,'\'),strcat(name,ext)));
  
    lbptest = preprocessing(DatabaseImage); % Feature vector of thr test image

  l= vec2mat(lbptest,length(lbptest));      %converting vector into matrix 
  l1 = predict(SVMModel,l)                  % predicting the label of the test image
  
  
  %showing the predicted label on test image
  
  figure
  imshow(DatabaseImage);
  title(l1);
   
end





