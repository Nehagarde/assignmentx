"""Print Processed Schedule for different days """


class TrackPrinter:
    """This Class has function to print conferences (Tracks)
    """
    def printtracks(self, datalist):
        """function to print"""
        lenthoffinallist = len(datalist)
        if lenthoffinallist == 0:
            print("Empty List. No Schedule was generated")
        else:
            cnt = 1
            for eachitem in datalist:
                print("Track no:" +str(cnt))
                cnt += 1
                for i in eachitem:
                    print(i)
                