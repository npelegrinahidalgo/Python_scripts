/*
Macro to open all Opera Phenix images and split channels and save them into different 
files for furhter data analysis (i.e. FRET)
*/

n=1 //number of paths to process

path= newArray(n);	


// All paths go below: follow this order (no_cells, ibd32, ibd33, zstack test)
//
//path[0]="/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/72h/ibd32_72h_no_cells__2022-12-16T12_37_37-Measurement 1/";
path[0]="/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/72h/ibd33_72h_10planes__2022-12-16T13_31_10-Measurement 2/";
//path[2]="/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/72h/ibd33_72h__2022-12-16T12_54_19-Measurement 1/";
//path[3]="/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/48h/ibd32_B2&3_zstack_test_48h__2022-12-15T12_17_42-Measurement 1/";



//The following is to generate an array containing all the different combinations needed for all the well IDs:

//well_ID = newArray("A1","A2","A3","A4","B1","B2","B3","B4");

for (i=0; i<path.length; i++){
	print(path[i]);
	if (i == 0) {
		well_ID = newArray("A1");//,"B1");
		FOV = Array.getSequence(31);
	}
	
	if  (i == 1) {
		well_ID = newArray("A2","A3","B1","B3","B4");
		FOV = Array.getSequence(31);
	}
	
	if  (i == 2) {
		well_ID = newArray("A1","A2","A3","A4","B1","B2","B3","B4");
		FOV = Array.getSequence(31);
	}
	
	if (i == 3) {
		well_ID = newArray("B2","B3");
		FOV = Array.getSequence(5);
	}
	
//	if statements above are used to define the wells and FOVs within each acquisition protocol as this changes depending
//  on the plate imaged or the condition (i.e. no cells, zstack test, etc)
	
	for (a=0; a<well_ID.length; a++){
		
		for (  j=1; j<FOV.length; j++){ //j starts at 1 because from array x index 0 will be 0, and there is no field of view labelled "F0"
		print(toString(well_ID[a]) + "_F" + j);
		
dir=path[i];



//Create folder where individual channel images will be saved (this will be a whole folder per well, with each FOV labelled respectively):

save_folder = dir + well_ID[a] + "_channels/";

File.makeDirectory(save_folder);


to_open = dir + well_ID[a] + "_F" + j + ".ome.tiff";

//Open image:

open(to_open);

rename("working_image");

//Set LUTs as accordingly (in this case: red, grays, yellow & green): CHECK THIS IS THE RIGHT ORDER IN THE IMAGE STACK!!!!

run("Red");
run("Next Slice [>]");
run("Grays");
run("Next Slice [>]");
run("Yellow");
run("Next Slice [>]");
run("Green");


//Split channels & z-project (avg intensity):

selectWindow("working_image");
run("Split Channels");

selectWindow("C1-working_image");
run("Z Project...", "projection=[Average Intensity]");
selectWindow("AVG_C1-working_image");
saveAs("Tiff", save_folder + well_ID[a] + "F"+ FOV[j] + "_AF647.tif");
close();
close();

selectWindow("C2-working_image");
run("Z Project...", "projection=[Average Intensity]");
selectWindow("AVG_C2-working_image");
saveAs("Tiff", save_folder + well_ID[a] + "F"+ FOV[j] + "_BF.tif");
close();
close();

selectWindow("C3-working_image");
run("Z Project...", "projection=[Average Intensity]");
selectWindow("AVG_C3-working_image");
saveAs("Tiff", save_folder + well_ID[a] + "F"+ FOV[j] + "_FRET.tif");
close();
close();

selectWindow("C4-working_image");
run("Z Project...", "projection=[Average Intensity]");
selectWindow("AVG_C4-working_image");
saveAs("Tiff", save_folder + well_ID[a] + "F"+ FOV[j] + "_AF488.tif");
close();
close();




}
}
}

print("Finished whole thing")
