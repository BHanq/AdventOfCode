import math

test = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

input = """
GGVGlqWFgVfFqqVZGFlblJPMsDbbMrDMpDsJRn
LwzHtwdLHHwDrzPZzzsJbJ
wdLTBvSvHvZVGCjhfN
HsSSnZVHjjssZnJpSJjBHHWgQGcgqqQLQdQFqNgWgqGNDg
rmmRwrtfThtTrbCrGGGcLBDTqDBNQLdL
mwPrrbzPfwvbzhwMMnnjHnBjZlnzMM
gjjdMBgdqdTpJpBcjgRRRlqnvrqfnZtrtZDw
zHShWLhCszCWHVbVzQWCPtQvNZRwtfftfNnrnftlfR
PzPSssHbVhCLFMJFcMFJJMjdJw
ZqJdtpfpjmpJjpnwWdttTCDLLTQFNTzTzrcqrQqc
MsSlBGvBsSGGSlbGsCgggNTgzNLczFQNrNQVQcFzFF
sGHHSGllhvMGhSRGCjtjtjnjnnmHWpWWtJ
tMdjQlHPHsGjsCtsCpwwqfhfnnFMDMrpfD
SbNvWvBRJRWwFSgppgSrfg
RNcNbvzJRcVLRVzTRFLjdHCQttdZdPlHstPl
QWqgpdBflpHNCNWNHHPm
VVMbbJsLFVMhrMJMmRjFNHwHjjCTGSSRFj
mbMsZzsLmVhJZrcLcJhLMtnqvBnZdggplDffvlnlvnDn
prnNnsFnZpnBNdNtFrNnzNQQwTTQZqTHTQJQMwHDMDlZ
jgfgcSmbLmhmcPShghRdmwJTQjTlqGlJQJHqQqGHqQ
hRVhPfbCgbVggLVRSSmRhRPhrrrnCzzsvCvrnvFnNppsvBtd
QJLNDWSWQdLFFFhLdt
npHhHMsfsjpZjznRtmrMCdBwFBFrBdmt
HsjHqRRfnnHRsgfHffZspgzqDGQSWbQTDNGhQhSqNPhDWWbT
bsCmFDsGZCNsDmLDLZBSHSJTHnrZQMQSSQ
jqRpwvfqnnRQrftdBMHddB
phpchwpzjpvwRzwcsnlFsssPCCGzDlsD
rMqzVQfrfVZWZhTdRTQL
cgmtFtjFFJDDtFvSFRZdLlhpHZddmwTZWh
FbcSTtctcvFTJNgtJDGNPnCqMPMfMBfznGVsrMCq
wLJfGJJPZLBfwSLGHbqmhhDHHhFDzfhv
FsnpFjVjplTQCspNlCDbzhMMbqvMvsgmHDqb
lRdlTdTddllpRQFRltVVdFRcwrtrcWWcPrrWPrPSrZWLPc
VGVZhTppGTfPnJVJrFqbsmbSSshHqWqRHF
llzDCzlBLdNcCddlMMNBdCCtWHbFqFRRRsHjWtRwSWqbmjWm
NbcMBBvzzMQLCDBVTQQPVrPQPPZVPp
cdcgfmQdqlqhzzPjzfwpwf
GLBGBDvbvRzGwtnnmPpp
ZRCZBRFSRvLRLFvvbLLFQdHMTHTlQlNqNmqFlWdH
vzjzvHtcHvJcDStLLGSShCbbfF
MWFFTVZRMmMgdQdSQLwQrQwbGw
gFTmgmVZssRsWZRNzJlBHHnnJDvzNPlP
rHrvHpmHZfdGDDGGZd
cTlMsNhllMhGchNPCBlhMQgVDdgDSSWVbWVwRQwRSgbV
lnBjnNNTTMnCTcChPNhMvtzvFGLtJrjFtHHHzHJm
lgpdZZMmGVVzVZzt
HfHLrHqbPbzJJzRJJPTl
HsLWWbDqFrqlqfbsbDqDBncpgFmmvpnmmgpvdvjcdM
GpNVbTpJJNvMBMVvJTGvhnWQQScllnhhWlhVSznV
ZjswwHHLZzGnjWjSjl
sHdftLLtgLfwdtPmHtMbNpMTpNqGRbPvTqPv
sHSNNhNwsllGSGGlWSGWSsFrrVbQrdmFrVrrmnrHmrHr
QQMRZDDRcrcnmRcV
fJfCPMJCzTMZSGsWwsWBwqQf
HwQZZJsHdqqsdJQGRgCgVGgSqgpcGG
ljWWbnPhjBlGpCRCnScSGg
hrrztWlbPjltjMPSdJDZSsHttwsZwD
VzzbmzvpvNhvBDqc
QHSJSQGCwJCGrGQjjcgcBFhdgqdqFdDNNw
rCGJtZrHhhtLRsth
TMWwCLPpMTThrvtMRJjbjRvmJs
fDzcHFfSfFQfZzZRJbdmmqqssqtbSW
WWgGZglcllgPBBCBNVGPNr
wrwwhpTpbqhqrshrrfrFfwfzRJGdNJHNmcFzCCzCRJGzGR
vMggvjQvgPvQjVLMMPSZqWNJGCzcNGdcdzHPPzcmCzPz
qDZWvBZVfDhbTtrp
LpDvHdjVghnjbGrn
FBBBPwwlBlwSfFTWPHPWWhmgngmmnPnmbsngngbGrb
FwftBSCSfWCtwfVQDvHHCMVvdQLQ
ZrQpQlSpNlqQCVnQBmdDqmWDqmWWBDBB
HsZMsJvZzLMHTRwWhgDwmfDBgdhWdf
RZvTzJGzRjFrVNVjlQrS
mqjMwfqlSSPmSrlPhwhVpGRcppWcpcGRcGWv
ssJDJJNgZNDWrRWcRpvr
ZTsTnnsLJQgPnfMwmnMrfm
qsVBvZqWLdfbfvLj
mPNRgmHBBGQrCbSbrdfCCSbC
PlQTGcTTcgGFQQGPTGllpqMzwzpVJZwBMssZ
FWGcNRLRLhwJJQfV
nzbzlDBHSpTDbpDpzHwCqhqwJJghQqQMCCBw
JnzndzpmJFmNsrrFsc
gmRwwDwfnRDJgwZLFQFFNGNQrFBmFbbm
CCVHVWWThSrjVGvbNj
WpdqpplppHCWzlClMMTTZJcJsdscJLLdbDDfZDgL
VNtCCMDllpBqDvtdCczTSgjHlzGSHSGZTZ
hPFPsQhhFhLnbsRnLFssdzcHdsSHSSHgjzHG
QPWPQrPPmbdnbWLFPrrBVrVDBqqNMVwttDtBvD
PPNNRggwgRRgHBhDtwhTwbDs
SFGSFSMCJFMrcrCMSSsbtrTbbZhBvtHhrTHD
MFfSMpflQLQflfLjnLmddsLdddqq
RcgbcrrFscVrwZVCgVGGmHppNNndWnGdNqddqqNqND
jTlSTBSTjLTvlvjjPtvMLlhHnftphtDFNFqDnDHWNddn
QBMQvzzjzvJPjFQMmwZJrgmCCJVRVbbc
CzPJsWCpvsNszsJsNsHlDhMrrJGjhrRVhRGgDDjG
tFFdbqFLFdwctQdfVhjRRghTcrjVRTDW
bwQtFLdLBdFmwnHnWHPBNnHCnp
CNTstGNslRRRstlmNmmTZZqfFwtqgwqgfBPSwSWwqgWq
hpDbcHbpSrcgqqzhhWVfqg
DDcLDjbMjCSsZRNlMv
MhHMCMNbzbMHlcqmGmrmWc
tnPggdZPBPgdtttJpdnwVBnmqQcvlQrQlfGqmfWffBcqWD
VPPwPPLPwLGFGLzCbG
rqBcBmjHTGfPbcVgPG
dlDpsdshzlldlDvsWlWvLQbQBbfLFLbPvbBGQBgG
BlBznnRWzlphphBnhZjZtNNCNmrNqjCqHwHN
mQBvmvBmmLJvvrLtttQrfhGlcRGfRhVGWJVChlRG
MzPswTsbTPPsNgMNszgzMpbMfcRcGflVGRfWSpFRlWWWFhcC
bcPsTbgbbTTwNZzTZzvdjdjtQQndZvdrvdmZ
hQzTQJFFZJrcdcdZFFrGFSVWVRWRwRgRHVMWDCDSWc
lPmpNBnnnsNBnLnfbfnCDWMvwRvDCCMPwwHWvM
HpjmffNlnqqhddTddFZjGJ
BwsLFFbHLbVCSCSFbsbFLsJbqnTtZrRMHTZtrTrZTcRRRRTq
lGhNhpPmmhpztZTBrcpjRqpB
QPzdfzBQNgFJSCwsdLbS
ZsZsSBTgffSCqSSfrMnnMwjqmqmnnnqwMm
bbPPbzVclcPzGNlvzVtmnDBnQmtnQLBjJVLn
zPFGplGGvdPbHplcbzzvdlNBTThgRpCTCTfhfsCCsSRZhR
CVLSVCLVZRsHcnzSRpdZZRCdPlmcMWDDlPNqMqtDMmqPMlDt
TBnGjfQrQJjhfWlPPmPQDNlmlP
fjhhGvjvvrTTBhvTBTbvGVRLzVnbSRZpHddspHRzLs
DDtWjfRfftWMLzSQjzzhWjjwRVPHqFbBbZHVwZBFvFwZvZ
JGllgCJlJsrCGPrCNTPdslvZVVNVbvBqNbbpbbFHpBwZ
CcPdnCdmCJjfcftWhtSL
pgpfddDGHWzDNGNGpRCQjCTFHZZQFQjcRT
bJlhqmMvnlrRQFtTthPVhZ
lvbJrlJMBwfzGNTddB
wpbJGGZpsjvtdWvGWF
HqqhBhBqhhNQHTSHqqNzRHVPvTvddWrjtrjFvrvdTdVP
NRLCRzlqHQtNRBLzQllhhZcgbggwmLDZpsgssDpwwD
pDzFzJFcVMcWJFJFzpLBsqWLZssshsGLGbsS
wqHqfvnfrRwQtdQRthhBbBbZLhPLnBTGsh
CfQqlqvtfHNvMVmzmmMCFDMc
GcgpNHvcSNvpSLphdhsLdQTsdWThhQ
wwzttPrrhQswdhnT
tjJjMJRbRbjztmjtjbgcRsNlgglHpDFSlSvg
VVLvLqqPVlvcqLLdwLbHpzcHSsbRJppHbHpF
CfjjCNGmMWhWjhWHWb
ZmGZffggrDqZvZtlbTqL
TTmmhvBvvHWzHpsPpstpLVdwwsLb
qflfFgNctNcCnCCNDnfFFNDwrslwZbPswwZbJLJZbrlPLL
FgQDDcncStCgtqccjSDTHWMThvhTQMBQhWvWRG
SqhVghPccSBhgSBqWBFNQNsHQHMjCCQQWCwQHN
fLZftnlttcbbtZbZlpZtttQjwsCQjRwwRDQspMRMNNQs
TfLtvbJtZmlbTTTtlJbFvVqPSgBdPqPhFSGBcd
pPPNDptcqtpcDztLDhhngnnJgJTmJwNnwm
HVVCsSClHGBCHslWHbSCGGVngTrJwnnJnQRRBrhQhgJhdm
WTWWWsvVlvGbWCFvjDftPpjqZLLtDz
wWclwtDwRvflvffB
sMMsGdsSTMrJZNqczfdvhvnzCnfv
rspppMjMspSTSMpgLjcPFmwPLmPHwb
tCdSMHtHtRFHdWSSJQSgrrrnghTNJN
BGfcvDsfvsqcvqfGvfGnNLhggBNQJNJQmpgQJm
sGfQDPDZzfDZzclwDzwsDlfjtbdHClFRCMWjbMFMRFWbdj
pJNCcvqCccsVvFCpqsmvWJfCBWgSzBBRrrBRDDgDrSbbgQbQ
TMLnLjjffwfwGdjQjDDBjBrDtztRSb
MdPLGhHnMZhlPHHTFfZvVCpmmmcFcVFC
SwFMfCMRCdQDdMbmdFfdbbnlcVncVCcgLqWcNNnCcWlW
hPjQzzhGzhpPrtPJPpPHrVgnqVVncVVnNHlqVnncNB
ptjGrptztpthtrtJJhTsGwFDZZDQmSdfZSwsRZSwfZ
rSSWWCWrdllHWpjcnFNnRCNjQp
bGwwJqGVGbGJVVhgbBgttGmBQjFsMjpMcMnnMBcQFNnsssvv
bfthwmfJfgwwmmwZqVJPHNHSZHWzSlDPrdDdSH
nmJccvclcbwmlbbvVbvsHwJJPCPNCNPnLBhrBPPLBhLhBgBP
MdRGtdDRTqWDMqtMDtQDRWSdLLBsrhLgBCgrgCgNNLPBfNMf
dRZQdDdRRSQWGsjZmwzjmlzsZH
PBGGMrTQTrTBpPQpLpSlwjwfjtlnfwbmGttw
fCsJCWJcvRCtwwjbCl
NsqcsfcvDHFVDJvdLQTrpdTTzTPpHr
rltrwsBTlrfGZggGBLGGNN
jhMnRQJVphMnbhvQjDZNqqZDNTNHZVHGHq
MRvbhQRQQChpvbjvMSvQnMcsFsfwwmlCwFwWcTWwrmPc
DDvLLLBnvrzvbvbmtv
TMwRjTRMGCwGGwrjQQnmrQrrQdhZ
MJPFHFTwgCGqGqgJMGDfSWcsnBSccgVDlnpW
flzVzNrdLNLJzrGlfdlzjrQDgFTpDgDmmmgFmqFDQjQh
CbnBcsZnPZVSnwvVsZbRhhBDpgFphgmgDgTppq
ZWnsWSnncSZsntZCbsswwJMzdLzlMdNMLtMVfrllMt
ZffSgNfgJgGCHZcZrpHrNJTLhqvSLTqQnvVTLvzvLTjV
tWFtHMwlBlDqjjzjnqvvlV
DRMPDtWHPFDBFFwWMFBmFRPgZpJfsffNGJNrGcsprrsmfg
wRZRmpZmlPqZjzGrdrGq
bBhQQFPQbPDVNzVNzdGWNdrf
QFbcDcDbLHgHBPDFRsSSMtmvRttMpCLS
MpWJVVJMcWvpRShcwpLGflmqzSfNdfNLdQzN
CDBTtCgtbjgCRrBrPBTQqzflNqjGdLzzmqffzq
rFgnnBbttDTPtHCDPrPMnpwVJhJvMZvpMvppRZ
sWTTmpsfsWppPTTsTVZWHVVZNvVcdcJvdN
DjjBzjhRHvvvSzdc
rMBjjrjbjrGDlgMlMrGjBgRLPTTwHMsfnFwFQPMPMnmFFm
QRRbDjjmPzNQwFDNmrQmzCbVHrMhBVrJLJJfMGGLtfJBHh
dsWcsqqWSWvnWnWcWGPJLBqhLBqGhBJHHH
ZWnPWgWgPnlbCDDwmmDbRZ
nfPqqfLqQnfHBSqnzztQjVmjfGRWJNGRWsJWJfmJ
TTMlMMlFDMGVGRsVJH
CbDbFDbvgTFFwgTDlDprhlPSqBzSnPdLPtPPHgznQqBQ
fJmWVfHqjfjhZCQZ
NcNzBNvgszQmzjnthZQC
LsLsgBNFmFgTFgGBBgcdMdvPDPDJWrlpVbGpJWqHDlHJHD
SllDdvzgdFDdlPJvbFDDSzFScPTRTNcwfZRwRhcwwNnRZTtf
WBpWBCLGVpLjHrHGGVhZNwcTVcNhVnRcNZ
LHLQLspHWQGpWCHnBvdzDJFlqvdsqgSgqS
GcTctDMjMhpMDRjLsMMsfDWFfdPCFNbnCPnvCPgW
JmvwqlBwnmfdFPFP
SvZqHSZqqHZZZBlllBwSwsRsMHpLjpLsMGtsMspGRT
ClLnCLfClLVllfLLcQjLBCfCmSHVsttsmtsVStDNVdppdsSp
PFrRMbWqMRwFRqRSqwqvMvMsGtgsdmssrgNtdmpNdDGgdt
bwJbPWPwFFPFSczCZzZZCcfjBJ
MwmBmzwJQTcTmfPVfZPwhhwHPH
jlnrglFLvbrGRFGnvFZdNNFfPZddPThVhdPH
RjbjpgbnLGvpLgzBqBpmWmmzqTMS
FnsSpttPnPbNCFDtsPnFHQZTQZgcwgDDTfrfTHMZ
mRjzRzlvBvhjZrQmMMwfZZNN
ldzddlzLRlRWdhjdRLjhRWtJbJbNtJJpJPbCbGCWNG
wBwmNZBTmzzcVcmpzZqdMgPjnLSVlPgDPdbMdg
flJvGtHffHDddddbHjnb
RstrhfrhhRGFQtRhtftvQhvFZpsmpWwNlWqcWTccBNWswqNp
DPWhbzDlQLLlQbLDlLhPhLFNNJqCFGqnNJCCSCnGPnGN
wvwjtvtdwfssvSJgFFvGGSCFcp
mtdrZwwJsrtddrHRtZWbVThLlBzVTzhHQWhB
TsRRWctsTJMQZllggc
zDvhpbprgGvpvVlVQlZpQMJVlQ
rrrvFvGCDhDSrrrvChCgSstBNTSftWBjTdfWBN
JJdssBcLVGrgbBHWrH
QZTptvmvmlZpRDlMMMZCQvnjjFnrjWGFbjnrnFGWgZrz
TMRplDMggtwlppTlvhsJJqdcqwVPSSNcLd
JjTCCrcRvccPLmMP
NfGFPZlNnwBfPlbbbQZGqLHgzLghSmMBzSgvzmDMhv
ZfbnNQpQnZGlGlGpWTddjdTJdpRPTrCj
gWLblMMggdWsdRJlblMRMMqWDvPvcPPPccJPJVTZVZThmcDP
rQFfGfrCHrjnrtNTcPShTSPvvVLtmm
fQrCfLrpLHnCHwslqzqsslswzqRW
zpJtGlJPMPTlTjGJCDGCDljpdnvhhWnZnZnDwwmvnWDWWvdd
sHrVrSrRRRLNgLVBqSsZmWwvwcvwZjmwngmdbn
QsQQBrrLHTjPpTQzzP
JDlzHHzzptRDmbTMrrVQ
dRRNqnCBnmrQsVQQ
wFPCBNFgwjPwhgFNztftpJRPpzRvvHtZ
DlBhrDBPPwMWwhWchW
ntSqbbSJFJNqzVzjCfMvfSlSRWccRL
mVlHtNVtqldbJVmNHmdTTBBgrQQgGsPQdrDgsP
HWHNbBgvNLdcvQMnSf
wqqqVPDPhqwszFwrrszFfMdWthLcMdfhthSQfJSt
qVPVwTzFwFDpDrPDzDPFDPlCHjBGjTmZGjbWWGZBRTNjjH
GVgdWjllSqgjdgHqqlfmhwcpwCzhvZwMcScv
nsJQbLRQsNnzQDQQPPBbRBRhfZwpZcvwpvvmLCcvpcmfMM
DRJtnnRbBBnPztsrPzRBPbsFFHqqVrqggjFWqrgWjTGgFq
hhZJQPJFHGGlcWWslpNN
VwwwJjvwMtrCnwjDNDzlfscWszWW
nVStCrMqbVwqVqSqwnLPhTJFdRgJHZSFRLTP
vPgMbbRhhvMvNjjLWsWQsHQmHwBrmmBzww
tFctDnVFpppHVBTdzdTQwl
FtSFqSptfJCqqJStZCqDpDJMhvLLgLMgQgjgGZgGgMPLZg
zwsWgSGWLSVhPWhtLgLWhPVNQTmDrDQttZpdQtdpQDDQZQ
fjCHcvvjMDrppCQpVV
VMqRnVJMVLPzbRWhGh
mjRmzQlzDzNHWwDZ
FBfJBGqnnpfSVGnpJbJVfNtCsJHWZvrsNJCZrCNsvN
fZPBnfPqSBqdfpFbVnVSjgdcLLgRLjmgRhLLghlR
FSFnTcppdQtnnDhtzDfg
ZLGVmBLBVwZCVjjGqGhVwVVgzzbMDtNNvszMmMffNDDvtM
VZPJjBZVqBZZBjqwVqllpSTphhQFPShWSQcW
hTRdcLrCLgplLvBFGvlL
nZDZqzbDbDzRZtVNDzDWGwslsllBFpnlpGvJssFG
zbqjNWQVmVPrrRjRdRhS
VpNCbVHlHHZfflVfmchctqFcqQQjZmZM
WDSRGgsSvgJSRrnWgqQhmjBqmhqrtLqmQm
znSGTgDJnsDGzgwCwlpbCNwHzVtl
sTTTrpHFFFqTnQbbvfJdDzHHDLVV
CjMtgMgRvbPfjjvB
mhMvlhhWClvqshNTQQqsNN
tWFtFBzbwdFrpmdhdm
qTqDjJjJQQqMjTDLJjNqNqPNdmpcSmhdmhhmcrWZpdPGddcc
RjNQLJNTTJDDJRHHjQqnMWtlvvVvbtBvRVzgzgwgVg
CGdQjwdJrbBmpmZZZlRWcb
NgtMPVstgSzBLzhgzgLgDRlcmDWRmlZvcSmDSvvp
LhNsgPPLFPPsNzMhhVzPsGJBFqwQGfnqfQjdGdGfwr
CNbNdbzjCZpPNzjmzjsCMRJvnnMRGnsvJGRs
wrtdwTLWFcFWdFgwRRsnJGnGfTGJfMsq
FttcwgBtgVLgPldQSNZBzBpz
DjRZrrRmttRFDvDrFTZsnWnHVSTSSJVZJH
dNNhLqlLLqdCzfMMlCfSncTVVWcHdcVsVdSVnT
QqppMfzMfqWCwbRQrwFrrttQ
dwGjHrtjsdhfCHnPSpfMfDPpPDWS
lmNzzlLbFqcqNgzpWMSvbbvDQDGWDp
LBmglgmqBqmrwCGhCjVtBC
tvHgWZCCprlgpWglCtjPhLmPmhVdJFSzVzdJVmmQ
fBnTTnNNBnwfnNqcBbBBTbGJQQJhSSdQJJsmdJFSQGSmVV
cMcDwFbRfFRlHCRCZrrp
ZFWmgghzBgwgjWBzjzmRWWMmsVwnVrsdVdwNrrpnnVrPCnCP
GLLbtGqllctqvGJvSlQbJGsPnVdsdpsTPLsVppBCTVss
tJBStGSvctvDDfczmRgRZjzDjZmgzH
FMrLmsQQSWzCZBhpQJTQQZ
dPPVncVvPBJDCPhwJD
fvHbbVHvqnvvvBzgLbbGGmrbMr
mrZzrzqDrhZqDddSFrCGLLLPQPQBJPJJBnQq
TgbpGblWlMsjgWlgMfpNRgbRHHBnHHHtLpCJPCPBnBLJtQQL
sbTlblTlvRbbGblbFcdDzccVcDVvzzzd
zMzfzlGwSBMMSCMzhsPgfcPcfcbhjQPt
FHHqJVdJmFmdVrJdJppthscjGtqRPRcccgcQbR
rvNJJpLrvvLnJvNFFvZZZBWznBWGSDCMnCwz

"""

def split_compartment(line):
    length_split = math.ceil(len(line) / 2)
    part1 = ""
    part2 = ""
    for x in range(0, length_split):
        part1 += line[x]
    for y in range(length_split, len(line)):
        part2 += line[y]

    return part1, part2

def find_shared_item(part1, part2 ,part3= None):
    shared = ""
    for x in part1:
        if x in part2 :
            if not part3 or x in part3:
                shared += x
                break
    return shared

def alpha_index(lettre):
    if 'a' <= lettre <= 'z':
        return ord(lettre) - ord('a') + 1
    elif 'A' <= lettre <= 'Z':
        return ord(lettre) - ord('A') + 27

def chal1():
    sum = 0
    for line in input.splitlines():
        if line != "":
            part1, part2 = split_compartment(line)
            shared_string = find_shared_item(part1,part2)

            for x in shared_string:
                sum += alpha_index(x)
    return sum

def chal2():
    sum = 0
    lines = []
    for line in input.splitlines():
        if line != "":
            lines.append(line)

    for x in range(0,math.floor(len(lines)/3)):
        shared_string = find_shared_item(lines[0+x*3] ,lines[1+x*3], lines[2+x*3])
        for x in shared_string:
            sum += alpha_index(x)
    return sum

print(chal1())
print(chal2())