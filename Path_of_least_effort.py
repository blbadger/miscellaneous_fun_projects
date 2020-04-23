def smallest_path_finder(maze):  
    ''' A function that takes a newline-separated string of strings of size nxn and returns 
    the size of the path from the top left corner to the bottom right that minimizes the 
    absolute values of differences between values.  Only moves left, right, up, or
    down are permitted. For example

    00
    00

    and

    11
    11

    and 

    123
    145
    111

    all have minimum total change of 0. Whereas

    0000
    0000
    1111
    0000

    has total change of 2.
    '''  

    # import standard library
    import copy

    # split maze string into parts of a list
    maze2 = [i for i in maze.split('\n')]
    N = len(maze2)
    maze = [[' '] * (N+2)]
    for i in range(N):
        maze.append([' '] + [int(j) for j in maze2[i]] + [' '])
    maze.append([' ']*(N+2))

    # initialize the variables needed for relaxation
    ls = [[0]*len(maze) for i in range(len(maze))]
    path = copy.deepcopy(ls)
    path[1][1] = 1
    target = [0, 0]

    def climb(maze, ls, path, target):
        '''a helper function that relaxes the weighted graph of
        elevations (maze) in order to make use of Dijkstra's 
        algorithm for minimum path in a weighted graph.
        '''
        count = 0
        for i, row in enumerate(maze):
            for j, obj in enumerate(row):
                if isinstance(maze[i][j], int):
                    for k in range(-1, 2, 2):

                        if isinstance(maze[i+k][j], int):
                            if path[i+k][j] == 0:
                                ls[i+k][j] = abs(maze[i+k][j] - maze[i][j]) + ls[i][j]
                                path[i+k][j] = 1
                            else:
                                if abs(maze[i+k][j] - maze[i][j]) + ls[i][j] < ls[i+k][j]:
                                    ls[i+k][j] = abs(maze[i+k][j] - maze[i][j]) + ls[i][j]
                                    count += 1

                        if isinstance(maze[i][j+k], int):
                            if path[i][j+k] == 0:
                                ls[i][j+k] = abs(maze[i][j+k] - maze[i][j]) + ls[i][j]
                                path[i][j+k] = 1
                            else:
                                if abs(maze[i][j+k] - maze[i][j]) + ls[i][j] < ls[i][j+k]:
                                    ls[i][j+k] = abs(maze[i][j+k] - maze[i][j]) + ls[i][j]
                                    count += 1

        if count > 0:

            # Speeds up the algorithm, at the expense of correctness: the following is 
            # only correct with high probability.  For an always-correct algorithm,
            # the following two lines may be removed.  This method returns the value
            # of smallest total change if the minimized value does not change after 
            # consecutive relaxation steps.  If running time is not an issue,
            # the climb function should be called whenever count > 0. 
            if ls[N][N] != target[-1] or ls[N][N] != target[-2]:
                target.append(ls[N][N])

                return climb(maze, ls, path, target)
            return ls[N][N]
        return ls[N][N]

    return climb(maze, ls, path, target)

# example input of elevations
maze = "\n".join([
'25638204721112757224308652381130669157903387072',
'17045705263852279105961978850448633254376505353',
'20019563090633934744266959296564182907195144514',
'99461666538339374091703143104622819650156953348',
'01789882399341801033135155488001040003510467318',
'69358328284225966481669481907167082808893416854',
'54021533619824102689221144142602929722293976824',
'27936218783557298360329322188176535321488399513',
'04777856270983183998297948975580341538634860531',
'25369238502810768527378608052066851833167916241',
'57482994981440788534801522676498332649378344211',
'15790135952416047179415854690501441540789258762',
'74282174441369481342674031399244445404075974219',
'83818081738174250106459715387939265752984462177',
'53370566904018824724826132508110532134571455708',
'47794799815400270818901818246283503219502670969',
'11245666464437609504279791853916250530957117844',
'92910117417334167220003122652821178456609505148',
'93217736469633220497769727235380673362002339461',
'04656269028639999229547294292103783647482007484',
'45427247204026544012007272440577213737953087794',
'71116140145549606616018392677244629871618952848',
'71764811100025622604609180109731227186954740428',
'05753996322552122614659190213982743834677379623',
'64066682437386397370824896138210604259168088080',
'85639769245163828906169758612653603202262187683',
'51861275353383438496829668662877470920158610500',
'54829224113240946151767451316721334813180145945',
'91334574961904069279023116427766581652171647922',
'82842503878566396115225794693961104341001434899',
'73497534684112710876215186207259882292330499259',
'14923236745856855720703654263711708335876313977',
'79435899010431877990748292627002976780425253620',
'50951972537664755906633835889071700738111233781',
'39033909300589228428168266937948594627906138272',
'95747792290955471693375509901475697570355416901',
'62303269438725214486380989630232255094849268181',
'88419590847734349346023539311683311309853242626',
'11306367903358584374753117573610238372691503271',
'19825496245872462503235682127422640353781754090',
'73096436578021531228100963724741715500618680656',
'34504940407540687569900455703645510766633065709',
'00720597392175815263974318703544647453023451921',
'80027816387169533487865453991712570604054097057',
'34112966240627928273536314035787349991017483098',
'40018235257510494256856220376281898150523148432',
'68638385456482726338791302515973042881683142486',
])

# example function call
print (smallest_path_finder(maze))